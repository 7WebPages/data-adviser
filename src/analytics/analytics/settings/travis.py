from .settings import *


INSTALLED_APPS += ('django_nose',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=core',
    '--cover-inclusive',
    '--cover-xml',
]
