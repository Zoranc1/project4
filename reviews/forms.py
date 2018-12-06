from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review



class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,label ='')
    class Meta:
        model = Review
        fields = ( 'content', )
        