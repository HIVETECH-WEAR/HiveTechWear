from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
PRODUCT_TYPE= (
            ('Men', 'Men'),
            ('Women', 'Women'),
        )


class Products(models.Model):
    class Meta(object):
        db_table='Products'
        
        
    name= models.CharField('name', max_length=25, blank=False)
    image=CloudinaryField('image', blank=False)
    description= models.CharField('description', max_length=100)
    price= models.IntegerField('price', blank=False)
    gender=models.CharField(max_length=20,blank=False, choices=PRODUCT_TYPE ) 
    
    