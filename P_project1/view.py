from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
#from .forms import userForm


def homePage(request):
    

    return render(request,"index.html")

def aboutPage(request):
    return render(request,"about.html")

def blogPage(request):
   
    return render(request,"blog.html")
def menuPage(request):
    return render(request,"menu.html")
def productsPage(request):
    return render(request,"products.html")
def reviewPage(request):
    return render(request,"review.html")
def thankyoupage(request):
    return render(request,"thankyou.html")

def contactPage(request):
   # fn = userForm
    data={}
    
    
    try:
        if request.method=="POST":
            
            name = str(request.POST.get('userName'))
            email = str(request.POST.get('userEmail'))
            number = int(request.POST.get('userNumber'))
            

            data={
                'name': name,
                'email': email,
                'number': number,
                'output': name,
            }
            
            return HttpResponseRedirect('/thankyou/')

    except:
        pass
    return render(request,"contact.html",data)

   # def contactPage(request):
    
   # try:
       # name = str(request.GET['userName'])
       # email = str(request.GET['useremail'])
       # number = int(request.GET['userNumber'])

  #  except:
     #   pass
   # return render(request,"contact.html", {'output':name})