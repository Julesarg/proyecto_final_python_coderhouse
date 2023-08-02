from django.shortcuts import render
from gallery.forms import *
from gallery.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

## back button ##
def on_backbutton_clicked(self, widget):
    self.webview.go_back()

## normal views requiere login ##
def gallery_home(request):
    return render(request, 'gallery_home.html')
@login_required
def search_fail(request):
    return render(request, 'gallery/search_fail.html')
@login_required
def add_success(request):
    return render(request, 'gallery/add_success.html')

## ADD ITEM OK ##
@login_required
def add_item(request):
    if request.method == "POST":
        myForm = ItemForm(request.POST, request.FILES)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            item = Item(item_name = inf['item_name'], item_created = inf['item_created'],item_price = inf['item_price'],item_description = inf['item_description'],item_genre = inf['item_genre'], item_material = inf['item_material'], item_image = inf['item_image'], item_stock = inf['item_stock'] )
            item.save()
        return render(request, 'add_success.html', {'myText':f'{myForm.as_p()}', 'item':item})
    else:
        myForm = ItemForm()
    return render(request, 'add_item.html', {'myForm': myForm})

## LIST GENRES OK ##
class PaintingList(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'paintings.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'
    
class SculptureList(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'sculptures.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class WoodMetalList(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'wood_and_metal.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class NftList(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'digital_assets.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class OtherList(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'other_craftings.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

## LIST DETAIL VIEW OK ##
class ItemDetail(LoginRequiredMixin,DetailView):
    model = Item
    template_name = 'detail_item.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

## delete view ok ##
class ItemDelete(LoginRequiredMixin,DeleteView):
    model = Item
    success_url ="/gallery/"     
    template_name = "item_confirm_delete.html"
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

## update view ok ##
class ItemUpdate(LoginRequiredMixin,UpdateView):
    model = Item
    success_url = '/gallery/'
    template_name = 'item_form.html'
    fields = ['item_name','item_price', 'item_description', 'item_image', 'item_stock', 'item_genre', 'item_material']
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

## busqueda de item por material ##
@login_required
def searchByMat(request):
    if request.GET['item_material']:
        item_material = request.GET['item_material']
        item = Item.objects.filter(item_material__icontains=item_material)
        if item:
            return render(request, 'search_success.html', {'item': item, 'item_material': item_material})
        elif not item:
            return render(request, 'search_fail.html',{'item': item, 'item_material': item_material})
        else:            
            return render(request, 'gallery_home.html')
    else:
        return render(request, 'search_fail.html')