from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact

def contact(request):
    if request.method=="POST":
        print('Post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        number=request.POST.get('number')
        print(name,email,content,number)

        if len(name)>1 and len(name)<60:
            pass
        else:
            messages.error(request,"Name should contain 2 to 60 characters")
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<60:
            pass
        else:
            messages.error(request,"Invalid email! Try again")
            return render(request,'home.html')
        
        if len(number)>2 and len(number)<13:
            pass
        else:
            messages.error(request,"Invalid number!")
            return render(request,'home.html')
        ins=models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,"Thank you for contacting!")
    return render(request,'home.html')
