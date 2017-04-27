from PIL import Image, ImageFilter
import itertools
import random

#Read image
im = Image.open( 'cow.png' )

divisor = int(input('chops?'))
regions = []

def getW(w):
	return w//divisor
def getH(h):
	return h//divisor

width = getW(im.width)
height = getH(im.height)

for x in range(0, divisor):
	for y in range(0,divisor):
		reg = im.crop((width*x, height*y,(width*(x+1)) , (height*(y+1))))
		regions.append(reg)

random.shuffle(regions)

n = 0;

for x in range(0, divisor):
	for y in range(0,divisor):
		im.paste(regions[n], (width*x, height*y,(width*(x+1)) , (height*(y+1))))
		n+=1

im.show()