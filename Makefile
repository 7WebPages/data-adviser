MANAGE=django-admin.py
SETTINGS=analytics.settings
CI_SETTINGS=analytics.settings.travis
DJANGO_PATH=`pwd`/src/analytics
COLLECTOR_PATH=`pwd`/src/collector

run:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) runserver 0.0.0.0:8000

test:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(CI_SETTINGS) $(MANAGE) test
	cd $(COLLECTOR_PATH); PYTHONPATH=`pwd` nosetests --with-coverage --cover-package=collector --cover-inclusive --verbosity=1 --cover-xml

collectstatic:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput

build:
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) migrate
	cd $(DJANGO_PATH); PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput

.PHONY: build
