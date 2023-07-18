from django.shortcuts import render

def admin_tools_home(request):
    return render(request, 'admin_tools_home.html')

def edit(request):
    return render(request, 'edit.html')