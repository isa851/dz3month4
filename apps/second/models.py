from django.db import models

# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length = 30, verbose_name = "Название")
    description = models.TextField(verbose_name = "Описание")
    logo = models.ImageField(verbose_name="Логотип")
    icon = models.ImageField(verbose_name="Иконка")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    locate = models.CharField(max_length=100, verbose_name="Локация")

    class Meta:
        verbose_name = "Данный"
        verbose_name_plural = "Данные сайта"
