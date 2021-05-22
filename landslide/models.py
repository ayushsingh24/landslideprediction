from django.db import models

class images(models.Model):
    moisture = models.URLField(max_length=50,blank=True)
    slope = models.URLField(max_length=50,blank=True)
    output = models.URLField(max_length=50,blank=True)