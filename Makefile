MANAGE=django-admin.py
SETTINGS=analytics.settings
DJANGO_PATH=`pwd`/src/analytics

test:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test

collectstatic:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput

build:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) migrate
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput

.PHONY: build
