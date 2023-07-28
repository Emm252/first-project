from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.


def home(request):
    return render(request,'index.html')
def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pass1 = request.POST['pass1']
        
        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        myuser.save()
        
        messages.success(request,"Your account has been successfully Created.")
        return redirect('signin')
        
    return render(request,"signup.html")
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html",{'fname':fname})
        else:
            messages.error(request, "Invalid username or password.")
            # Instead of redirecting, render the same "signin" page with error message
            return render(request, "signin.html")
    return render(request,"signin.html")
def signout(request):
    logout(request)
    messages.success(request,"logged out Successfully")
    return redirect('index')

