#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kai Sforza'
SITENAME = 'kaictl'
SITEURL = 'https://blog.kaictl.me'
SITELOGO = SITEURL + '/images/profile.png'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'

THEME = "themes/flex"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'post_stats', 'render_math']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll

STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/keybase.txt': {'path': 'keybase.txt'},
    'extras/custom.css': {'path': 'static/custom.css'},
}

DEFAULT_PAGINATION = 10
MARKUP = ('mkd', )
CUSTOM_CSS = 'static/custom.css'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "kaictl"
GOOGLE_ANALYTICS = "UA-42514434-2"

BROWSER_COLOR = '#333'

SOCIAL = (('linkedin', 'https://linkedin.com/in/kaictl'),
          ('github', 'https://github.com/KaiSforza'),
          ('gitlab', 'https://gitlab.kaictl.me/kaictl'),
          ('twitter', 'https://twitter.com/kaictl'),
          ('reddit', 'https://reddit.com/u/kaictl'),
          )

MAIN_MENU = True