from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Ad(models.Model):
    """
    A single Blog post
    """
    class Meta:
        permissions = (
            ('can_publish', 'Can publish a blog post'),
        )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', null=False, default=1, on_delete=models.SET_DEFAULT) 
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, default='0.00')
    
    def __str__(self):
        return self.title
        
class AdImage(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    ad = models.ForeignKey(Ad, related_name='images', null=False, on_delete=models.CASCADE) 
    
        