# Generated by Django 4.2.2 on 2023-07-30 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_age_gender_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gender',
            name='user',
        ),
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]