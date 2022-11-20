"""P_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from P_project1 import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homePage, name='home'),
    path('about/', view.aboutPage,name='about'),
    path('blog/', view.blogPage,name='blog'),
    path('products/', view.productsPage,name='products'),

    path('contact/', view.contactPage,name='contact'),
    path('menu/', view.menuPage,name='menu'),
    path('review/', view.reviewPage,name='review'),
    path('thankyou/', view.thankyoupage,name='thankyou'),

    
]
