import math
import os
import sys
from PIL import Image, ImageDraw

while True:
    try:
        tilesize = int(input('Enter your desired tile size in pixels (Example: 16 will be a 16x16 tile):'))
        break
    except:
        print("You must enter an integer!")

folder = 'toslice/'
toslice = os.listdir('toslice/')
for entry in toslice:
    im = Image.open(os.path.join(folder, entry))
    rows = im.size[0] / tilesize
    rows = math.ceil(rows)
    cols = im.size[1] / tilesize
    cols = math.ceil(cols)
    dirname = entry.rstrip('.png')
    os.mkdir(os.path.join(folder, dirname))
    for x in range(rows):
        for y in range(cols):
            box = (0 + y * tilesize, 0 + x * tilesize, tilesize + y * tilesize, tilesize + x * tilesize)
            region = im.crop(box)
            slice = Image.new('RGBA', (tilesize, tilesize), color=255)
            mask=Image.new('L', slice.size, color=255)
            draw=ImageDraw.Draw(mask)
            draw.rectangle((0,0,tilesize,tilesize), fill=0)
            slice.putalpha(mask)
            slice.paste(region, (0,0))
            outfile = "r" + str(x+1) + "c" + str(y+1) + ".png"
            slice.save(os.path.join(folder, dirname, outfile))
