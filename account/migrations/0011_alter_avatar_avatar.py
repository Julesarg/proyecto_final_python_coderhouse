# Generated by Django 4.2.2 on 2023-07-31 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_avatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, default='settings.MEDIA_ROOT/avatar/default.jpg', null=True, upload_to='avatar'),
        ),
    ]
