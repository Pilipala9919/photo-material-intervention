#!/usr/bin/env python3
"""Create a privacy-safe resized image reference and OpenAI messages JSON."""
from PIL import Image,ImageOps
from pathlib import Path
import argparse,base64,json
p=argparse.ArgumentParser()
p.add_argument('image');p.add_argument('prompt')
p.add_argument('--output',required=True);p.add_argument('--max-side',type=int,default=1365)
p.add_argument('--quality',default='hd');a=p.parse_args()
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
im=ImageOps.exif_transpose(Image.open(a.image).convert('RGB'))
im.thumbnail((a.max_side,a.max_side),Image.Resampling.LANCZOS)
ref=out.with_suffix('.reference.jpg');im.save(ref,quality=92,exif=b'')
r=im.width/im.height
size='1024x1536' if r<.85 else ('1536x1024' if r>1.18 else '1024x1024')
data=base64.b64encode(ref.read_bytes()).decode()
body={'messages':[{'role':'user','content':[{'type':'text','text':Path(a.prompt).read_text()},{'type':'image_url','image_url':{'url':'data:image/jpeg;base64,'+data}}]}],'generation_config':{'size':size,'quality':a.quality,'n':1}}
out.write_text(json.dumps(body))
print(json.dumps({'output':str(out),'reference':str(ref),'size':size,'exif_removed':True}))
