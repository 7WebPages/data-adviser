import os
import sys

from .runner import SpiderRunner

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'analytics/'
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analytics.settings')
sys.path.append(BASE_DIR)

os.chdir(BASE_DIR)

from django.core.wsgi import get_wsgi_application  # noqa
application = get_wsgi_application()

from core import models  # noqa

if __name__ == '__main__':
    spiders = models.Provider.objects.filter(enabled=True).all()
    runner = SpiderRunner(spiders)
    runner.update_categories()
