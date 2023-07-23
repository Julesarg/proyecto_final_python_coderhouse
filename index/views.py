from django.shortcuts import render

def index_home(request):
    return render(request, 'index_home.html')

def about(request):
    return render(request, 'about.html')

def message(request):
    return render(request, 'message.html')