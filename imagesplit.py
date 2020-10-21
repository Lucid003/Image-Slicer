import math
import os
import sys
from PIL import Image, ImageDraw
 
#temporary code for single use
#im = Image.open("48x48.png")


'''entries = os.listdir('images/')
toProcess = []
for image in entries:
    toProcess.apend(Image.open(images))'''

print('Enter your desired tile size in pixels (Example: 16 will be a 16x16 tile):')
while True:
 try:
  tilesize = int(input('Enter your desired tile size in pixels (Example: 16 will be a 16x16 tile):'))
  break
 except:
  print("You must enter an integer!")
  
tilesize = input()
tilesize = int(tilesize)

with os.scandir(/') as entries:
    for entry in entries:
        im = Image.open(entry)
        rows = im.size[0] / tilesize
        rows = math.ceil(rows)
        cols = im.size[1] / tilesize
        cols = math.ceil(cols)
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
                      dirname = entry.rstrip('.png')
                      os.mkdir(dirname)
                      outfile = "r" + str(ir+1) + "c" + str(ic+1) + ".png"
                      slice.save(os.path.join(path, dirname, outfile)
                
'''while ir != rows:
    while ic != cols:
        box = (0 + ic * tilesize, 0 + ir * tilesize, tilesize + ic * tilesize, tilesize + ir * tilesize)
        region = im.crop(box)
        slice = Image.new('RGBA', (tilesize, tilesize), color=255)
        mask=Image.new('L', slice.size, color=255)
        draw=ImageDraw.Draw(mask)
        draw.rectangle((0,0,tilesize,tilesize), fill=0)
        slice.putalpha(mask)
        slice.paste(region, (0,0))
        outfile = "r" + str(ir+1) + "c" + str(ic+1) + ".png"
        slice.save(outfile)
        ic += 1
    ir +=1
    ic = 0'''
