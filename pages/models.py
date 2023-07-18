from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_created = models.DateField()
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=999)

    class Genre(models.IntegerChoices):
        PAI = 1, "Paintings"
        SCL = 2, "Sculptures"
        NFT = 3, "Nfts"
        HDC = 4, "Handcraft (Wood, Metal, etc)"  
        OTH = 5, "Other"
    item_genre = models.PositiveSmallIntegerField(
        choices=Genre.choices,
        default=Genre.PAI
    )
    
    class Material(models.IntegerChoices):
        DIG = 1, "Digital Asset"
        WOO = 2, "Wood"
        STO = 3, "Stone"
        MET = 4, "Metal"  
        CAN = 5, "Canvas & Paint"
        CER = 6, "Ceramics"
        CLA = 7, "Clay"
        OTH = 9, "Others"
    item_material = models.PositiveSmallIntegerField(
        choices=Material.choices,
        default=Material.CAN
    )
    item_image = models.ImageField(null=True, blank=True, upload_to="images/")
    item_stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Product Name: {self.item_name}, Price: {self.item_price}, Genre: {self.item_genre}, Material: {self.item_material}, Stock: {self.item_stock}, Img: {self.item_image}, Published: {self.item_created}, Description: {self.item_description}'