from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from adds.models import Ad

# Create your models here.
class review(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='review', null=False, default=1, on_delete=models.SET_DEFAULT) 
    product = models.ForeignKey(Ad, related_name='review', null=False, default=1, on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        