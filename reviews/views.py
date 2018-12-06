from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.

def make_review(request,id):
    
        saved_review=ReviewForm(request.POST)
        savedReview = saved_review.save(commit=False)
        savedReview.author =request.user
        savedReview.product_id =id
        
        
        savedReview.save()
        review_blog = savedReview
        
        return redirect('view_product',id=id,)
    
