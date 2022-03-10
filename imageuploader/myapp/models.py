from django.db import models

# Create your models here.
class Image(models.Model):
     photo = models.ImageField(upload_to="myimage",height_field=None,width_field=None,max_length=100)
     date = models.DateTimeField(auto_now_add=True)