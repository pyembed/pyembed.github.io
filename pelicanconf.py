#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.markdown import PyEmbedMarkdown
from pyembed.rst import PyEmbedRst

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

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {},
    'pyembed.markdown': {}
  }
}

PyEmbedRst().register()

PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc']

URL_ENDING = 'index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
