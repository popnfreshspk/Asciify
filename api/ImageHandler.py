import tornado.web
import json
from image_to_ascii import AsciiFy
from urlparse import urlparse, parse_qs

class BaseHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('AsciiFy Me')

class ImageHandler(tornado.web.RequestHandler):
	def post(self):
		invert = self.get_argument('invert', 'True')
		x_dim = int(self.get_argument('x', 150))
		y_dim = int(self.get_argument('y', 150))
		
		im = self.request.body
		print len(im)
		art = AsciiFy(im, 
					  invert = invert,
					  x_dim = x_dim,
					  y_dim = y_dim)
		self.write(art)
