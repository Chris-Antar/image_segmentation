# Generated by Django 4.0.4 on 2023-03-07 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_multipleimage_delete_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
