from django.shortcuts import render
from django.urls import reverse_lazy
from gallery.forms import *
from gallery.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView



# def custom_404(request, exception):
#     return render(request, 'custom_404.html', status=404)

## normal views##
def gallery_home(request):
    return render(request, 'gallery_home.html')
def search_fail(request):
    return render(request, 'gallery/search_fail.html')
def add_success(request):
    return render(request, 'gallery/add_success.html')
# def modify_success(request):
#     return render(request, 'gallery/modify_success.html')


##ADD ITEM OK##
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


##LIST GENRES OK##
class PaintingList(ListView):
    model = Item
    template_name = 'paintings.html'
class SculptureList(ListView):
    model = Item
    template_name = 'sculptures.html'
class WoodMetalList(ListView):
    model = Item
    template_name = 'wood_and_metal.html'
class NftList(ListView):
    model = Item
    template_name = 'digital_assets.html'
class OtherList(ListView):
    model = Item
    template_name = 'other_craftings.html'

##LIST DETAIL VIEW OK##
class ItemDetail(DetailView):
    model = Item
    template_name = 'detail_item.html'

##delete view##
class ItemDelete(DeleteView):
    model = Item
    success_url ="/gallery/"     
    template_name = "item_confirm_delete.html"

## update view##
class ItemUpdate(UpdateView):
    model = Item
    success_url = '/gallery/'
    template_name = 'item_form.html'
    fields = ['item_name','item_created', 'item_price', 'item_description', 'item_image', 'item_stock', 'item_genre', 'item_material']

##back button#############################
def on_backbutton_clicked(self, widget):
    self.webview.go_back()

## busqueda de item por material ##
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
        # return redirect('../errorMessage')
        return render(request, 'paintings.html')
    
    ##FALTAN VISTAS DE ERROR##