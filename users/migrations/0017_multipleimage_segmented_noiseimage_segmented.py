# Generated by Django 4.0.4 on 2023-03-09 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_noiseimage_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='multipleimage',
            name='segmented',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noiseimage',
            name='segmented',
            field=models.BooleanField(default=False),
        ),
    ]