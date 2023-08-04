from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Cart(models.Model):
    class Meta(object):
        db_table= 'cart'

    
    