"""buy_sell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls
from adds import urls as adds_urls
from adds.views import show_all_adds
from django.conf import settings
from django.views.static import serve


from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_all_adds, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(accounts_urls)),
    path('adds/', include(adds_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
    
