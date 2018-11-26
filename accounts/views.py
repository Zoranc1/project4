from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, BuyerProfileForm, SellerProfileForm



def show_profile(request):
    return render(request,'profile.html')


def signup_buyer(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = BuyerProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = BuyerProfileForm.save(commit=False)
            profile.user = user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
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
            profile = SellerProfileForm.save(commit=False)
            profile.user = user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse('Something went wrong..... ')
    else:
        form = SignUpForm()
        profile_form =SellerProfileForm()
        return render(request, 'registration/signup_seller.html', {'user_form': form, 'profile_form':profile_form})    