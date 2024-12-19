#!/usr/bin/python3

#convert to PGM and do something on it (scale height or offset it)
#
# for any of the following libraries run:
#
# py -m pip install <name>
#
# if it is not already included in to your python3 install
# firehound on mwll channel on discord.


import math
import os
import sys
import platform
from PIL import Image, ImageDraw, ImageFont
import csv
import pygame
from pygame.locals import *  # this is for QUIT to work

import numpy as np
import matplotlib.pyplot as plt
off=0 #65536/4 #here we define the offset

imgdir='/Program Files (x86)/Electronic Arts/Crytek/Crysis Wars/Mods/MWLL/Game/Levels/Multiplayer/TC/TC_Warresst'
img='terrain.pgm'
outimg='terrain_scaled.pgm'

os.chdir( imgdir )
os.listdir( os.curdir )

## read it in

with open(img) as f:
  lines = f.readlines()

  # Ignores commented lines
  for l in list(lines):
    if l[0] == '#':
      lines.remove(l)

  print ('Making sure it is ASCII format (P2)')
  assert lines[0].strip() == 'P2' 
  
  print ( 'Format:' , lines[0])
  sizeX=int(lines[1][0:lines[1].index(" ")])
  sizeY=int(lines[1][lines[1].index(" "):])
  print ( 'Values per line:', sizeX)
  print ( 'Lines:         :', sizeY)
  print ( 'Max. DataValue :', lines[2] )
  print ( 'Creating the data array:' )
  stuff= ["" for y in range(sizeY+1)]   
  
  # Converts data to a list of integers
  data = []
  X=0
  Y=0
  print ( 'Processing data array:' )
  ## go thru and scale it down
  for Y in range( 0, sizeY):
    stuff[Y]=list(map(int, lines[3+Y].split()))
    print ('L:',Y,'/','\r',end="")
    for X in range ( 0, sizeX):
      stuff[Y][X] = str(int(int(off+(stuff[Y][X])/2)))  #here we halve the height 

  print ('')
print ('Accesing Output file:')
## open the output file
outstream = open(outimg,'w')
#header
outstream.write('P2'+'\n')
print ('P2'+'\n',end="")
outstream.write(str(sizeX)+' '+str(sizeY)+'\n')
print (str(sizeX)+' '+str(sizeY)+'\n',end="")
outstream.write('65535'+'\n')
print ('65535'+'\n',end="")
for line in stuff:
  #data
  print (len(" ".join(line)),'\r',end="")
  outstream.write(" ".join(line)+'\n')
outstream.close
