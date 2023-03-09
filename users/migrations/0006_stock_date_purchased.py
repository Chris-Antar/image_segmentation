# Generated by Django 4.0.4 on 2022-06-13 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_stock_percentage_change_1y_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date_purchased',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]