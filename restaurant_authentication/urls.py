from django.urls import path

from . import views

urlpatterns = [

    # path('<slug:allrest_name>/', views.manu, name ='manu'),
    path('', views.home, name='home'),



]