from django.shortcuts import render



def home(request):

    return render(request,'restaurant_authentication/home.html')