#!/usr/bin/env python3
"""Inspect image geometry without exposing EXIF metadata."""
from PIL import Image, ImageStat
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('image'); p.add_argument('--json',action='store_true')
a=p.parse_args()
im=Image.open(a.image).convert('RGB')
w,h=im.size
thumb=im.copy(); thumb.thumbnail((512,512))
st=ImageStat.Stat(thumb)
out={
 'width':w,'height':h,
 'aspect_ratio':round(w/h,4),
 'orientation':'portrait' if h>w else ('landscape' if w>h else 'square'),
 'mean_rgb':[round(x,1) for x in st.mean],
 'thumbnail_size':list(thumb.size),
 'exif_disclosed':False
}
print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else '\n'.join(f'{k}: {v}' for k,v in out.items()))
