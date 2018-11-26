from django.db import models
from django.contrib.auth.models import User



class SellerProfile(models.Model):
   
    image = models.ImageField(upload_to='avatars',default='avatars/anonimus.png', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='seller') 
    vat_number = models.CharField(max_length=30, null=True, blank=True)
    
    
   
class BuyerProfile(models.Model):
   
    image = models.ImageField(upload_to='avatars',default='avatars/anonimus.png', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='buyer') 
    
    