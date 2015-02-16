import json
from glob import glob
import os
from pprint import pprint

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def load_pages():
	pages = {}
	for json_path in glob(os.path.join(FILE_PATH, 'pages', '*.json')):
		with open(json_path) as json_file:
			loaded = json.load(json_file)
			name = loaded['title']['link']
			pages[name] = loaded
	page_names = "'{}'".format("', '".join(pages.keys()))

	load_info = 'Loaded pages: {}'.format(page_names)
	print(load_info)

	return pages
