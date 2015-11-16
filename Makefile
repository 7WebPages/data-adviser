MANAGE=django-admin.py
SETTINGS=analytics.settings

test:
        PYTHONPATH=`pwd`/src/analytics DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test
