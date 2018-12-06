from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group,User
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from adds.models import Ad
from .forms import SignUpForm, BuyerProfileForm, SellerProfileForm


def signup_buyer(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = BuyerProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            seller_group =Group.objects.get(name='buyer')
            seller_group.user_set.add(user)
            return redirect('all_ads')
        else:
            return HttpResponse('Something went wrong..... ')
    else:
        form = SignUpForm()
        profile_form =BuyerProfileForm()
        return render(request, 'registration/signup_buyer.html', {'user_form': form, 'profile_form':profile_form})

        
def signup_seller(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = SellerProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            seller_group =Group.objects.get(name='sellers')
            seller_group.user_set.add(user)
            return redirect('home')
        else:
            return HttpResponse('Something went wrong..... ')
    else:
        form = SignUpForm()
        profile_form =SellerProfileForm()
        return render(request, 'registration/signup_seller.html', {'user_form': form, 'profile_form':profile_form})   
        
def profile(request,id):
    seller = get_object_or_404(User, pk=id)
    ads = Ad.objects.filter(seller_id=id)
    return render(request, "profile.html", {'seller': seller,'ads':ads})        