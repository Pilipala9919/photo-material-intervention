#!/usr/bin/env python3
"""Create a deterministic side-by-side review sheet."""
from PIL import Image,ImageOps,ImageDraw
import argparse
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('result');p.add_argument('--output',required=True);p.add_argument('--width',type=int,default=1600);a=p.parse_args()
imgs=[ImageOps.exif_transpose(Image.open(x).convert('RGB')) for x in (a.source,a.result)]
cell=a.width//2
can=[]
for im in imgs:
 r=min(cell/im.width,1200/im.height); z=im.resize((round(im.width*r),round(im.height*r)),Image.Resampling.LANCZOS)
 bg=Image.new('RGB',(cell,1200),(24,24,24));bg.paste(z,((cell-z.width)//2,(1200-z.height)//2));can.append(bg)
out=Image.new('RGB',(a.width,1200));out.paste(can[0]);out.paste(can[1],(cell,0));ImageDraw.Draw(out).line((cell,0,cell,1200),fill=(240,220,170),width=4);out.save(a.output,quality=92)
print(a.output)
