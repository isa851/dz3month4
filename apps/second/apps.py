from tabnanny import verbose
from django.apps import AppConfig


class SecondConfig(AppConfig):
    name = 'apps.second'
    verbose_name = "2) данные"
