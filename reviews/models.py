from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from adds.models import Ad

# Create your models here.
class Review(models.Model):
    content = models.TextField(max_length=200)
    author = models.ForeignKey(User, related_name='reviews', null=False, default=1, on_delete=models.SET_DEFAULT) 
    product = models.ForeignKey(Ad, related_name='reviews', null=False, default=1, on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        