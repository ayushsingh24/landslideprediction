from django.db import models

class images(models.Model):
    moisture = models.ImageField('Moisture')
    slope = models.ImageField('Slope')
    output = models.ImageField('Output')