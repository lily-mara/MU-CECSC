#!/usr/bin/env python3
import tornado.autoreload
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import os

from setup import load_pages

PAGES = load_pages()


class MainHandler(tornado.web.RequestHandler):
	def get(self, page):
		page_name = page.split('.')[0]

		page_info = PAGES.get(page_name)

		if page_info is None:
			self.clear()
			self.set_status(404)
			self.finish('<html><body>That page does not exist.</body></html>')
			return

		page_content = page_info.get('content')
		page_title = page_info.get('title')

		if page_info is None:
			self.clear()
			self.set_status(404)
			self.finish('<html><body>That page does not exist.</body></html>')
			return

		page_options = {
			'content': page_content,
			'title': page_title['name'].split(' '),
			'page_list': [i['title'] for i in PAGES.values()]
		}

		self.render('contents.html', **page_options)


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		page_options = {
			'page_list': [i['title'] for i in PAGES.values()]
		}

		self.render('index.html', **page_options)


HANDLERS = [
	(r'/', IndexHandler),
	(r'/(.*)', MainHandler)
]

SETTINGS = {
	'debug': False,
	'static_path': os.path.join('static'),
	'template_path': os.path.join('templates')
}

APPLICATION = tornado.web.Application(HANDLERS, **SETTINGS)

if __name__ == '__main__':
	define('port', default=4000, type=int)
	tornado.options.parse_command_line()
	APPLICATION.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
