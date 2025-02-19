from django.db import models

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to="myimage") # upload_to: store picture in file name which I give.
    date = models.DateTimeField(auto_now_add=True)
