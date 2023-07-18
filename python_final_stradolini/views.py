from django.http import HttpResponse
from django.shortcuts import render

def messages(resquest):
    return HttpResponse('messages view')