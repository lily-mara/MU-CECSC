#!/usr/bin/env python3
import tornado.autoreload
import tornado.ioloop
import tornado.web
import os
import json

pages = None

def load_pages():
	global pages

	pages = {}
	with open('pages/who.json') as json_file:
		pages['who'] = json.load(json_file)

class MainHandler(tornado.web.RequestHandler):
	def get(self, page='index.html'):
		page_name = safe_get(page.split('.'), 0)
		
		print(safe_get(pages, page_name))
		
		options = {}
		self.render(page, **options)
		
def safe_get(col, ind, default=''):
	try:
		return col[ind]
	except IndexError:
		return default

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
	load_pages()
	application.listen(4000)
	tornado.ioloop.IOLoop.instance().start()
