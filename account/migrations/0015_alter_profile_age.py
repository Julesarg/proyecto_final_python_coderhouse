# Generated by Django 4.2.2 on 2023-07-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_profile_delete_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
    ]