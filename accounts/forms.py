from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BuyerProfile, SellerProfile


class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
class BuyerProfileForm(forms.ModelForm):
    
    class Meta:
        model = BuyerProfile
        fields = ('image',)  
        
        
class SellerProfileForm(forms.ModelForm):
    
    class Meta:
        model = SellerProfile
        fields = ('image','about','vat_number','bank_name','iban','bic')        