from django.shortcuts import render
from gallery.forms import *
from gallery.models import *


def gallery_home(request):
    return render(request, 'gallery_home.html')

def paintings(request):
    return render(request, 'paintings.html')

def sculptures(request):
    return render(request, 'sculptures.html')

def woodcraft(request):
    return render(request, 'woodcraft.html')

def digital_assets(request):
    return render(request, 'digital_assets.html')

def other_craftings(request):
    return render(request, 'other_craftings.html')

def add_p(request):
    if request.method == "POST":
        myForm = ItemForm(request.POST, request.FILES)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            item = Item(item_name = inf['item_name'], item_created = inf['item_created'],item_price = inf['item_price'],item_description = inf['item_description'],item_genre = inf['item_genre'], item_material = inf['item_material'], item_image = inf['item_image'], item_stock = inf['item_stock'] )
            item.save()
        return render(request, 'gallery_home.html', {'myText':f'{myForm.as_p()}'})
    else:
        myForm = ItemForm()
    return render(request, 'add_item.html', {'myForm': myForm})