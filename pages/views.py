from django.shortcuts import render
from pages.forms import *
from pages.models import *


def pages_home(request):
    return render(request, 'pages_home.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page2.html')

def add_p(request):
    if request.method == "POST":
        myForm = ItemForm(request.POST, request.FILES)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            item = Item(item_name = inf['item_name'], item_created = inf['item_created'],item_price = inf['item_price'],item_description = inf['item_description'],item_genre = inf['item_genre'], item_material = inf['item_material'], item_image = inf['item_image'], item_stock = inf['item_stock'] )
            item.save()
        return render(request, 'pages_home.html', {'myText':f'se ha creado el item {item.item_material}, {item.item_image}, {item.item_genre}'})
    else:
        myForm = ItemForm()
    return render(request, 'add_item.html', {'myForm': myForm})