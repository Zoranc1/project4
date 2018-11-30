from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.

def make_review(request,id):
    
    if request.method =='POST':
        saved_review=ReviewForm(request.POST)
        savedReview = saved_review.save(commit=False)
        savedReview.author =request.user
        savedReview.ad_id =id
        
        
        savedReview.save()
        review_blog = savedReview
        
        return redirect('read_ad',id=id,)
    else:
        
        form= ReviewForm()
   
    
        return  redirect('read_ad',{'form':form})

