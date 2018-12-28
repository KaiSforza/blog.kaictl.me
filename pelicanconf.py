#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Wallace'
SITENAME = 'GTmanfred'
SITEURL = 'https://blog.gtmanfred.com'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'

THEME = "themes/bootstrap4"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Git Repositories', 'https://github.com/gtmanfred/'),
    ('Feeds', '/feeds/'),
)
EXTRA_PATH_METADATA={'extra/robots.txt': {'path': 'robots.txt'}}

DEFAULT_PAGINATION = 10
MARKUP = ('mkd', )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "gtmanfred"
GOOGLE_ANALYTICS = "UA-42514099-1"
