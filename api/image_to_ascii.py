from PIL import Image
from PIL import ImageOps
from StringIO import StringIO
import requests
import xlwt, sys

def find_color(brightness, colors):
	b = int(brightness/3.64285)
	return colors[b]

def PrepImage(image, x_dim, y_dim):
	if len(image) < 1000:
		im = Image.open(StringIO(requests.get(image)))
	else:
		im = Image.open(StringIO(image))
	im = im.resize((x_dim, y_dim))

	return im

def AsciiFy(image, invert=True, x_dim=150, y_dim=150):

	im = PrepImage(image,  
				   x_dim = x_dim, 
				   y_dim = y_dim)

	if(invert == 'False'):
		colors = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
	else:
		colors = """ .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""

	output = ""
	for pixely in range(0,y_dim-1):
		output += '\n'
		for pixelx in range(0,x_dim-1):
			color = im.getpixel((pixelx,pixely))
			color = 0.21*color[0] + 0.71*color[1] + 0.07*color[2]
			
			output+= find_color(color, colors)
	
	return output
