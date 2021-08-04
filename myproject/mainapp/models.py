from datetime import datetime

from django.db import models


class Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'product brand'
        verbose_name_plural = 'product brands'


class Category(models.Model):
    title = models.CharField(max_length=50, help_text='Категория продукта')
    brand = models.ManyToManyField(Brand, blank=True)

    def __str__(self):
        return self.title


# class Status(models.Model):
#     status = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='Status img/')


class Products(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    mini_about = models.TextField(max_length=150)
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=70, default='None', help_text='sale or new')
    # status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='ProductImages/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    theme = models.CharField(max_length=30)
    message = models.TextField(blank=False)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ChekOut(models.Model):
    name = models.CharField(max_length=50)
    username = models.TextField(max_length=70)
    password = models.TextField(max_length=70)
    company = models.CharField(max_length=70)
    email = models.EmailField()
    title = models.CharField(max_length=70)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=70)
    sity = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    zip_code = models.PositiveIntegerField()
    # country = models.CharField(max_length=150)
    # regions = models.CharField(max_length=150)
    phone = models.PositiveIntegerField()
    mobil_phone = models.PositiveIntegerField()
    fax = models.CharField(max_length=100)
    about = models.TextField(max_length=5000)


class Blog(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=70)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(max_length=5000)
    created_add = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='New Message', help_text='answered')