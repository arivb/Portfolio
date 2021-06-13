from django.shortcuts import redirect, render
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def homepage(request):
    if not request.user.is_authenticated:
        return redirect("signup")
    return render(request,'articles/index.html')
def about(request):
    return render(request,'articles/about.html')
def projects(request):
    return render(request,'articles/projects.html')    
def contacts(request):
    return render(request,'articles/contacts.html')    
def game(request):
    return render(request,'articles/game.html')
def login(request):
    #if request.method=="Post":
    if request.method=="POST":
        name=request.POST["name"]
        phonenumber=request.POST["phonenumber"]
        print(request.GET)
        print(request.POST)
        user=authenticate(request,name=name,phonenumber=phonenumber)
        
        if user is not None:
            form=login(request,user)
            messages.success(request,f"welcome{name}")
            return redirect("homepage")
        else:
            messages.info(request,'account does not exist please sign in')
    
    #form=AuthenticationForm()
    form=LoginForm()
    return render(request,'articles/login.html', {"form":form}) 

def signup(request):
    #if request.method=="Post":
    if request.method=="POST":
        form=SignUpForm(request.POST)
        print(request.GET)
        print(request.POST)
        if form.is_valid():
            data=form.save()
            print(data)
            data.save()
            messages.success(request,"you account has been created")
            return redirect("login")
    else:
        form=SignUpForm()
    return render(request,'articles/signup.html', {"form":form}) 
