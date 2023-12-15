"""
URL configuration for MyDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from django.shortcuts import HttpResponse,render


def index(request):
    # return HttpResponse('<h1>Hey CSITian')
    context= {
        'username_data':username,
        'address_data': address,
    }
    return render(request,'index.html',context)

def summer(request,a,b):
    return HttpResponse(f"The sum is {a+b}")

def multiplication(request):
    username = request.GET.get('user')                                              #hit http://localhost:8000/queryparams/?user=sushant in browser
    address = request.GET.get('address')
    return HttpResponse(f'<h2><b>Username is {username} and address is {address}')      #hit http://localhost:8000/queryparams/?user=sushant&address=Dharan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('sum/<int:a>/<int:b>/',summer),
    path('queryparams/',multiplication)
]
