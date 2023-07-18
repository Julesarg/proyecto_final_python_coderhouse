from django.shortcuts import render

def account_home(request):
    return render(request, 'account_home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html')