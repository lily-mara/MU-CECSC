#!/usr/bin/env python3

import tornado.autoreload
import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
	def get(self, page='index.html'):
		options = {}
		self.render(page, **options)

handlers = [
		(r'/', MainHandler),
		(r'/(.*)', MainHandler)
		]

settings = {
		'debug': True,
		'static_path': os.path.join('static'),
		'template_path': os.path.join('templates')
		}

application = tornado.web.Application(handlers, **settings)

if __name__ == '__main__':
	application.listen(4000)
	tornado.ioloop.IOLoop.instance().start()
