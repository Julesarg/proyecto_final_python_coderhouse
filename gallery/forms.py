from django import forms
from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_created','item_price', 'item_description','item_image', 'item_stock','item_genre','item_material']