"""Admin config"""

from django.contrib import admin
from django.apps import apps

# Obtain all the app from the Eye app and register all
app = apps.get_app_config('eye')

for model_name, model in app.models.items():
    admin.site.register(model)
