from django.db import models


class Product(models.Model):
    vendor_code = models.PositiveIntegerField(verbose_name='Артикул', primary_key=True)
    category = models.CharField(verbose_name='Категория', max_length=50)
    manufacturer = models.CharField(verbose_name='Производитель', max_length=50)
    model_name = models.CharField(verbose_name='Модель', max_length=100)
    dealer_price = models.PositiveIntegerField(verbose_name='Дилер UAH')
    retail_price = models.PositiveIntegerField(verbose_name='РРЦ', blank=True, null=True)

    def __str__(self):
        return str(self.vendor_code) + ' ' + self.model_name

# Create your models here.
