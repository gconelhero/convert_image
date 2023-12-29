from django.db import models
from django.conf import settings

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    date = models.DateTimeField( auto_now_add=True)
    