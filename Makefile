MANAGE=django-admin.py
SETTINGS=analytics.settings
DJANGO_PATH=`pwd`/src/analytics

test:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test

