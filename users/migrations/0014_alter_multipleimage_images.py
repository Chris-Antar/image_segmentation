# Generated by Django 4.0.4 on 2023-03-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_multipleimage_title_multipleimage_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimage',
            name='images',
            field=models.FileField(upload_to='profile_pics'),
        ),
    ]