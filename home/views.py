from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate , login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        if name == "" or email == "" or desc == "":
            messages.error(request, 'Input All Fields To Send Us A Message')
        else:
            contact = Contact(name=name,email=email,desc=desc)
            contact.save()
            messages.success(request, 'Your Message has been sent!')
    return render(request, 'contact.html')

def login_page(request):
    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        # print(name, password)
        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, "Incorrect Credentials")
    return render(request, 'login_page.html')

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # print(name, email, password, password2)
        if name != "" and email != "" and password == password2:
            user = User.objects.create_user(name, email, password)
            user.save()
            return render(request, 'user_home.html')
        else:
            messages.error(request, "Check Input/Fill All Fields/Passwords Not Matching")
    return render(request, 'sign_up.html')

def user_home(request):
    if request.user.is_authenticated:
        return render(request, 'user_home.html')
    else:
        return redirect("login_page")

def logout_user(request):
    print("LOGOUT BUTTON PRESS")
    logout(request)
    return redirect("/")