"""restaurant_management URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from restaurant_authentication import views
from restaurant_package import views as package
from single_service import views as single
from features import views as features
from item import views as item
from pamment import views as pamment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant_authentication.urls')),
    path('list/', views.Restaurant_authenticationList.as_view()),
    path('packagelist/', package.Restaurant_package_List.as_view()),
    path('singlelist/', single.Single_service_list.as_view()),
    path('featureslist/', features.featureslist.as_view()),
    path('itemlist/',item.Item_List.as_view()),
    path('pammentlist/',pamment.Pamment_List.as_view()),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
