from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    

    return render(request,"index.html")

def aboutPage(request):
    return render(request,"about.html")

def blogPage(request):
    return render(request,"blog.html")
def contactPage(request):
    return render(request,"contact.html")
def menuPage(request):
    return render(request,"menu.html")
def productsPage(request):
    return render(request,"products.html")
def reviewPage(request):
    return render(request,"review.html")