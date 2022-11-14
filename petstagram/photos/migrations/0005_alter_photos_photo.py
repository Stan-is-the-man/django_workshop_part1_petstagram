# Generated by Django 4.1.1 on 2022-10-12 06:30

from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photos_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', validators=[petstagram.photos.models.validate_image_size_less_than_5mb]),
        ),
    ]