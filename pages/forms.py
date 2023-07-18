from django import forms
from .models import *

class ItemForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    item_created = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    item_price = forms.IntegerField()
    item_description = forms.CharField(max_length=999)
    item_image = forms.ImageField()
    item_stock = forms.IntegerField()    
    item_genre = forms.ChoiceField(
        choices=(
            (1,('Paintings')),
            (2,('Sculptures')),
            (3,('Nfts')),
            (4,('Handcraft (Wood, Metal, etc)')),
            (5,('Other'))
        )
    )
    item_material = forms.ChoiceField(
        choices=(
            (1,('Digital Asset')),
            (2,('Wood')),
            (3,('Stone')),
            (4,('Metal')),
            (5,('Canvas & Paint')),
            (6,('Ceramics')),
            (7,('Clay')),
            (8,('Others'))
        )
    )    