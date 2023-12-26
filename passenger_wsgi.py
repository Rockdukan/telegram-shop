# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1100210/data/www/xn--80aadc4a6bn.xn--p1ai')
sys.path.insert(1, '/var/www/u1100210/data/www/xn--80aadc4a6bn.xn--p1ai/venv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
