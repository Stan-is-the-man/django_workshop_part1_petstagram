# Generated by Django 4.1.1 on 2022-10-14 05:45

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_alter_photo_description'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('date_and_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='photos.photo')),
            ],
        ),
        migrations.RemoveField(
            model_name='photolike',
            name='to_photo',
        ),
        migrations.DeleteModel(
            name='PhotoComment',
        ),
        migrations.DeleteModel(
            name='PhotoLike',
        ),
    ]
