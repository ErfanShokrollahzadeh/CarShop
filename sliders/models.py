from django.db import models


class Slider(models.Model):
    objects = None
    image_url = models.CharField(max_length=2083)
