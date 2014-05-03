#!/usr/bin/env python3
import tornado.autoreload
import tornado.ioloop
import tornado.web
import os
import json
from glob import glob

pages = None

def load_pages():
	global pages

	pages = {}
	for file_path in glob('pages/*'):
		basename = os.path.basename(file_path)
		file_name, extension = os.path.splitext(basename)
		with open(file_path) as json_file:
			pages[file_name] = json.load(json_file)
	page_names = "'" + "', '".join(list(pages.keys())) + "'"
	print('Loaded pages: {}'.format(page_names))

class MainHandler(tornado.web.RequestHandler):
	def get(self, page='index.html'):
		page_name = safe_get(page.split('.'), 0)
		
		page_info = safe_get(pages, page_name)
		page_content = safe_get(page_info, 'content')

		if page_content is None and page != 'index.html':
			self.clear()
			self.set_status(404)
			self.finish("<html><body>That page does not exist.</body></html>")
			return
			
		print(json.dumps(pages, indent = ' ' * 4))
		
		options = {
				'content': page_content,
				'page_list': [pages[i]['title'] for i in pages]
		}
		
		if page == 'index.html':
			self.render(page, **options)
			return

		self.render('contents.html', **options)
				
		
def safe_get(col, ind, default=None):
	try:
		return col[ind]
	except IndexError:
		return default
	except KeyError:
		return default
	except TypeError:
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
