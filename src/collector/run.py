import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'analytics/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analytics.settings')
sys.path.append(BASE_DIR)

os.chdir(BASE_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()