import math
import os
import sys
from easygui import *
from PIL import Image, ImageDraw

while True: # basic input validation
    try:
        tilesize = int(enterbox("Enter your desired tile size in pixels (Example: 16 will be a 16x16 tile:"))
        # tilesize = int(input('Enter your desired tile size in pixels (Example: 16 will be a 16x16 tile):'))
        break
    except:
        print("You must enter an integer!")

choices = ('Image', 'Folder', "Cancel")
decision = buttonbox("Would you like to split an image or a folder of images?", "Image Splitter", choices)
if decision == "Folder":
    folder = diropenbox("", "Select a folder with images to slice...")
    # folder = 'toslice/' # change this to your desired location
    toslice = os.listdir(folder) # gets all objects in your folder, even folders so make sure it's just images
elif decision == "Image":
    toslice = []
    toslice.append(fileopenbox("Select a file to split...", "Image Splitter"))
elif decision == "Cancel":
    exit()
for entry in toslice:
    dirname = entry.rstrip('.png') # folder name for output
    dirname = dirname.rstrip('.jpg') # folder name for output
    dirname = dirname.rstrip('.gif') # folder name for output
    if decision == "Folder":
        im = Image.open(os.path.join(folder, entry)) # open image
        os.mkdir(os.path.join(folder, dirname)) # makes output folder
    elif decision == "Image":
        im = Image.open(entry)
        os.mkdir(dirname) # makes output folder
    rows = im.size[1] / tilesize 
    rows = math.ceil(rows) # for images that aren't squares
    cols = im.size[0] / tilesize
    cols = math.ceil(cols) # same as above comment
    # os.mkdir(os.path.join(folder, dirname)) # makes output folder
    for x in range(rows):
        for y in range(cols):
            # box is a square representing the desired tilesize at the desired tile location
            box = (0 + y * tilesize, 0 + x * tilesize, tilesize + y * tilesize, tilesize + x * tilesize)
            region = im.crop(box) # copies image data located at box
            slice = Image.new('RGBA', (tilesize, tilesize), color=255)
            mask=Image.new('L', slice.size, color=255) # alpha mask for odd image sizes,
            draw=ImageDraw.Draw(mask) # above-mentioned mask
            draw.rectangle((0,0,tilesize,tilesize), fill=0) 
            slice.putalpha(mask) # applies alpha mask to slice
            slice.paste(region, (0,0)) # applies copied (region) image data to slice
            outfile = "r" + str(x+1) + "c" + str(y+1) + ".png" # prepping output file name
            if decision == "Folder":
                slice.save(os.path.join(folder, dirname, outfile)) # saving output file
            else:
                slice.save(os.path.join(dirname, outfile)) # saving output file
msgbox("Splitting Completed!", "Image Splitter", "End Program")
