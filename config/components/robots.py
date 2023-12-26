"""robots.txt settings"""
# https://django-robots.readthedocs.io/en/latest/


ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24

ROBOTS_SITEMAP_URLS = [
    'http://www.example.com/sitemap.xml',
]

ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'

ROBOTS_USE_HOST = False

ROBOTS_USE_SCHEME_IN_HOST = True

ROBOTS_USE_SITEMAP = False
