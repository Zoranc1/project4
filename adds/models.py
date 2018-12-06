from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
TYPE_CHOICES = [
    ('Oil','Oil'),
    ('Wine','Wine'),
    ('Cheese','Cheese'),
    ]
class Ad(models.Model):
    """
    A single Ad post
    """
    class Meta:
        permissions = (
            ('can_publish', 'Can publish a ad post'),
        )
    title = models.CharField(max_length=200)
    content = models.TextField()
    sku = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    seller = models.ForeignKey(User, related_name='ads', null=False, default=1, on_delete=models.SET_DEFAULT) 
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, default='0.00')
    category =  models.CharField(max_length=10, choices=TYPE_CHOICES) 
    
    def __str__(self):
        return self.title
        
class AdImage(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    ad = models.ForeignKey(Ad, related_name='images', null=False, on_delete=models.CASCADE) 
    
        