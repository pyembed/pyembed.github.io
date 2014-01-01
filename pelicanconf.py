#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.markdown.extension import PyEmbedExtension

AUTHOR = u'Matt Thomson'
SITENAME = u'PyEmbed'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

THEME = 'theme'

MD_EXTENSIONS = [PyEmbedExtension(), 'toc']

PLUGIN_PATH = 'plugins'
PLUGINS = ['extract_toc']

URL_ENDING = 'index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
