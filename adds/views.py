from django.shortcuts import render, get_object_or_404,redirect
from .models import Ad
from .forms import AdForm

from reviews.forms import ReviewForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

# Create your views here.
def home_page(request):
    
    return render(request,'home.html')
    
def show_all_ads(request):
    ads= Ad.objects.filter(published_date__lte=timezone.now())
    return render(request,'ads/all_ads.html',{'ads':ads})
    
def ad_category(request,category):
    ads = Ad.objects.filter(category=category,published_date__lte=timezone.now())
    
    return render(request,'ads/category.html',{'category':ads})


def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

    
def user_can_edit_add(request, ad):
    wrote_the_add = ad.seller == request.user
    superuser = request.user.is_superuser
    return wrote_the_add or superuser 

def read_ad(request,id):
    product = get_object_or_404(Ad, pk=id)
    product.views +=1
    product.save()
    form=ReviewForm()
    
    can_edit = user_can_edit_add(request, product)

    return render(request, "ads/dispey_ad.html",{'ad':product,'can_edit':can_edit,'form':form})
    
def edit_ad(request, id):
    post = get_object_or_404(Ad, pk=id)
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES, instance=post)
        form.save()
        return redirect(read_ad, id)
    else:        
        form=PostForm(instance=post)
        return render(request, "ads/post_ad.html", {'form': form }) 

@permission_required('adds.add_post')
def write_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        post=form.save(commit=False)
        post.seller = request.user
        post.save()
        return redirect(read_ad, post.id)
    else:        
        form=AdForm()
        return render(request, "ads/adding_ad.html", {'form': form }) 
        


    
@permission_required('adds.can_publish')
def get_unpublished_ad(request):
    ads = Ad.objects.filter(published_date__isnull=True)
    return render(request, "ads/unpubliched.html", {'ads': ads})    



@permission_required('adds.can_publish')
def publish_ad(request, id):
    post = get_object_or_404(Ad, pk=id)
    post.published_date = timezone.now()
    post.save()
    return redirect(get_unpublished_ad)







