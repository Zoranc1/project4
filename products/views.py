from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from .forms import ProductForm

from reviews.forms import ReviewForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

# Create your views here.
def home_page(request):
    return render(request,'home.html')

    
def show_all_products(request):
    products = Product.objects.filter(published_date__lte=timezone.now())
    return render(request,'products/all_products.html',{'products':products})
    
    
def products_by_category(request,category):
    products = Product.objects.filter(category=category, published_date__lte=timezone.now())
    return render(request,'products/category.html',{'category':products})


def view_product(request,id):
    product = get_object_or_404(Product, pk=id)
    product.views +=1
    product.save()
    form=ReviewForm()
    return render(request, "products/display_product.html", {'product':product, 'form':form})
    
    
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        form.save()
        return redirect(view_product, id)
    else:        
        form=ProductForm(instance=post)
        return render(request, "products/post_product.html", {'form': form }) 


@permission_required('products.add_product')
def write_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        product=form.save(commit=False)
        product.seller = request.user
        product.save()
        return redirect(view_product, product.id)
    else:        
        form=ProductForm()
        return render(request, "products/add_product.html", {'form': form }) 
        


    
@permission_required('products.can_publish')
def get_unpublished_products(request):
    products = Product.objects.filter(published_date__isnull=True)
    return render(request, "products/unpublished.html", {'products': products})    



@permission_required('products.can_publish')
def publish_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.published_date = timezone.now()
    product.save()
    return redirect(get_unpublished_products)







