# Generated by Django 4.2.2 on 2023-07-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('I prefer not to tell', 'I prefer not to tell')], max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
