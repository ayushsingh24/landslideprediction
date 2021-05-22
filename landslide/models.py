from django.db import models

class images(models.Model):
    moisture = models.URLField(max_length=200,blank=True)
    slope = models.URLField(max_length=200,blank=True)
    output = models.URLField(max_length=200,blank=True)