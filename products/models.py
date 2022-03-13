from django.db import models

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    page_url = models.CharField(max_length=200)

class Slider(models.Model):
    objects = None
    img_urls = models.CharField(max_length=2083)

class Navbar(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=2083)

class Footer(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=2083)

class Slider2(models.Model):
    objects = None
    img_urls = models.CharField(max_length=2083)

class LastestNew(models.Model):
    object = None
    email_adress = models.CharField(max_length=100)