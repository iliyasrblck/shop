from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.urls import reverse

# Create your models here.

class Users(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    birthday = jmodels.jDateField(null=True, blank=True )


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


    def get_absolute_url(self):
        return reverse('sabzeno:PR-CG-list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    slug = models.SlugField(max_length=100, verbose_name='اسلاگ')
    description = models.TextField(verbose_name='توضیحات', max_length=5000)
    inventory = models.PositiveIntegerField(verbose_name='موجودی', default=0)
    price = models.PositiveIntegerField(verbose_name='قیمت', default=0)
    offer = models.PositiveIntegerField(verbose_name='تخفیف', default=0)
    new_prices = models.PositiveIntegerField(default=0, verbose_name='قیمت بعد از تخفیف')

    cerated = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = jmodels.jDateTimeField(auto_now=True, verbose_name='بروز رسانی زمان')

    class Meta:
        ordering = ['-cerated']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-cerated']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def get_absolute_url(self):
        return reverse('sabzeno:PR-detail', args=[self.slug, self.id])

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام ویژگی')
    value = models.CharField(verbose_name='مقدار ویژگی', max_length=100)
    Product = models.ForeignKey(Product, related_name='feature', on_delete=models.CASCADE, verbose_name='محصول')

    def __str__(self):
        return self.name + ": " + self.value


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='محصول')
    image_file = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    cerated = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-cerated']
        indexes = [
            models.Index(fields=['cerated']),
        ]
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر ها'
