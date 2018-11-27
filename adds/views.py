from django.shortcuts import render, get_object_or_404,redirect
from .models import Ad
from .forms import AdForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

# Create your views here.
def show_all_adds(request):
    adds= Ad.objects.filter(published_date__lte=timezone.now())
    return render(request,'profile.html',{'adds':adds})


def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def in_authors(request,id):
    inauthors= is_in_group(request.user, 'authors')

    return render(request, "/base.html",{'is_authors':inauthors})
    
def user_can_edit_add(request, post):
    wrote_the_add = post.author == request.user
    is_editor = is_in_group(request.user, 'editors')
    superuser = request.user.is_superuser
    return wrote_the_add or superuser or is_editor


def get_index(request):
    posts = Ad.objects.filter(published_date__lte=timezone.now())
    return render(request, "adds/displey_ad.html", {'posts': posts})
    
def read_ad(request,id):
    post = get_object_or_404(Ad, pk=id)
    post.views +=1
    post.save()
    
    can_edit = user_can_edit_add(request, post)

    return render(request, "adds/dispey_ad.html",{'post':post,'can_edit':can_edit})
    
def edit_ad(request, id):
    post = get_object_or_404(Ad, pk=id)
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES, instance=post)
        form.save()
        return redirect(read_ad, id)
    else:        
        form=PostForm(instance=post)
        return render(request, "adds/post_ad.html", {'form': form }) 

@login_required
def write_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        post=form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(read_ad, post.id)
    else:        
        form=AdForm()
        return render(request, "adds/adding_ad.html", {'form': form }) 
        


    
@permission_required('adds.can_publish')
def get_unpublished_ad(request):
    adds = Ad.objects.filter(published_date__isnull=True)
    return render(request, "adds/unpubliched.html", {'adds': adds})    



@permission_required('adds.can_publish')
def publish_ad(request, id):
    post = get_object_or_404(Ad, pk=id)
    post.published_date = timezone.now()
    post.save()
    return redirect(get_unpublished_ad)







