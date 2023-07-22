from django.db import models
import datetime

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_created = models.DateField(("Date"), default=datetime.date.today)
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=999)
    item_image = models.ImageField(null=True, blank=True, upload_to="images/")
    item_stock = models.PositiveSmallIntegerField()

    genre_choices = (
    ('Paintings', 'Paintings'),
    ('Sculptures','Sculptures'),
    ('Nfts','Nfts'),
    ('Handcraft (Wood, Metal, etc)','Handcraft (Wood, Metal, etc)'),
    ('Other','Other')
    )
    item_genre = models.CharField(max_length=40, blank=True, null = True, choices = genre_choices)

    material_choices = (
    ('Digital Asset', 'Digital Asset'),
    ('Wood','Wood'),
    ('Stone','Stone'),
    ('Metal','Metal'),
    ('Canvas & Paint','Canvas & Paint'),
    ('Ceramics','Ceramics'),
    ('Clay','Clay'),
    ('Other','Other')
    )
    item_material = models.CharField(max_length=40, blank=True, null = True, choices = material_choices)    

    def __str__(self):
        return f'Product Name: {self.item_name}, Published: {self.item_created}, Price: {self.item_price}, Description: {self.item_description}, Img: {self.item_image}, Stock: {self.item_stock}, Genre: {self.item_genre}, Material: {self.item_material}'