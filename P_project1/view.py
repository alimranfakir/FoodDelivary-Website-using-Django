from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    

    return render(request,"index.html")

def aboutPage(request):
    return render(request,"about.html")

def blogPage(request):
   
    return render(request,"contact.html")
def menuPage(request):
    return render(request,"menu.html")
def productsPage(request):
    return render(request,"products.html")
def reviewPage(request):
    return render(request,"review.html")

def contactPage(request):
    data={}
    
    
    try:
        if request.method=="POST":
            
            name = str(request.POST['userName'])
            email = str(request.POST['useremail'])
            number = int(request.POST['userNumber'])
            

            data={
                    'name': name,
                    'email': email,
                    'number': number,
                    'output': name,
            }
            return HttpResponseRedirect('/about/')

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