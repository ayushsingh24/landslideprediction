from django.db import models

class images(models.Model):
    moisture = models.ImageField('Moisture',upload_to="images/")
    slope = models.ImageField('Slope',upload_to="images/")
    output = models.ImageField('Output',upload_to="images/")