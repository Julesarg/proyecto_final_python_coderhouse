# Generated by Django 4.2.2 on 2023-07-22 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_created',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_genre',
            field=models.CharField(blank=True, choices=[('Paintings', 'Paintings'), ('Sculptures', 'Sculptures'), ('Nfts', 'Nfts'), ('Handcraft (Wood, Metal, etc)', 'Handcraft (Wood, Metal, etc)'), ('Other', 'Other')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_material',
            field=models.CharField(blank=True, choices=[('Digital Asset', 'Digital Asset'), ('Wood', 'Wood'), ('Stone', 'Stone'), ('Metal', 'Metal'), ('Canvas & Paint', 'Canvas & Paint'), ('Ceramics', 'Ceramics'), ('Clay', 'Clay'), ('Other', 'Other')], max_length=40, null=True),
        ),
    ]
