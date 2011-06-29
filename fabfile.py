from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.apps.alerts',
        'lettuce.django',
    ),
    'SITE_ID': 1,
}

main_app = "alerts"
full_name = "armstrong.apps.alerts"
tested_apps = (main_app, )
pip_install_first = True
