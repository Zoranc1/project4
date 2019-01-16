from django.db import models
from django.contrib.auth.models import User



class SellerProfile(models.Model):
   
    image = models.ImageField(upload_to='avatars',default='avatars/anonimus.png', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='seller')
    about  = models.TextField(max_length=300, null=True, blank=True)
    vat_number = models.CharField(max_length=30, null=True, blank=True)
    bank_name = models.CharField(max_length=30, null=True, blank=True)
    iban = models.CharField(max_length=30, null=True, blank=True)
    bic = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return '{0} {1}'.format(self.user.first_name,self.user.last_name)
    
    
   
class BuyerProfile(models.Model):
   
    image = models.ImageField(upload_to='avatars',default='avatars/anonimus.png', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='buyer') 
    
    def __str__(self):
            return '{0} {1}'.format(self.user.first_name,self.user.last_name)