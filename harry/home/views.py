from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def blog(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def register_view(request):
    return render(request, 'register.html')

