from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index_home(request):
    return render(request, 'index_home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def message(request):
    return render(request, 'message.html')