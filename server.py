import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from api.ImageHandler import *

from tornado.options import define, options
define("port", default=9999)

class ApiApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", BaseHandler),
			(r"/image", ImageHandler)
		]
        
        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(ApiApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
