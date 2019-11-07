# Generated by Django 2.2.1 on 2019-10-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20191029_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.TextField(default='Album Image'),
        ),
        migrations.AddField(
            model_name='band',
            name='band_photo',
            field=models.TextField(default='Artist Image'),
        ),
        migrations.AlterField(
            model_name='band',
            name='band_bio',
            field=models.TextField(default='Artist Biography'),
        ),
    ]