from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(max_length = 30, verbose_name = "Названия сайта")
    description = models.TextField(verbose_name = "Описание сайта")   


    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"