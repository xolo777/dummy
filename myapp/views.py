from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

def home(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})
    
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password != confirm_password:
            return HttpResponse("Passwords do not match!")
        elif len(password) < 8:
            return HttpResponse("Password must be at least 8 characters long!")
        elif not any(char.isdigit() for char in password):
            return HttpResponse("Password must contain at least one digit!")
        else:
            return HttpResponse("Registration successful!")
        #Handle registration logic here
      
    return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
