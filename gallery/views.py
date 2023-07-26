from django.shortcuts import render
from gallery.forms import *
from gallery.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


def gallery_home(request):
    return render(request, 'gallery_home.html')

# def paintings(request):
#     return render(request, 'paintings.html')

# def sculptures(request):
#     return render(request, 'sculptures.html')

# def wood_and_metal(request):
#     return render(request, 'wood_and_metal.html')

# def digital_assets(request):
#     return render(request, 'digital_assets.html')

# def other_craftings(request):
#     return render(request, 'other_craftings.html')

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










class CourseDetail(DetailView):
    model = Item
    template_name = 'mainApp/course_detail.html'
class CourseCreate(CreateView):
    model = Item
    success_url = '/mainApp/course/list'
    fields = ['name', 'course_number']
class CourseUpdate(UpdateView):
    model = Item
    success_url = '/mainApp/course/list'
    fields = ['name', 'course_number']
class CourseDelete(DeleteView):
    model = Item
    success_url = '/mainApp/course/list'