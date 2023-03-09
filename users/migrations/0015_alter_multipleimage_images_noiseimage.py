# Generated by Django 4.0.4 on 2023-03-08 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_alter_multipleimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimage',
            name='images',
            field=models.FileField(upload_to='media'),
        ),
        migrations.CreateModel(
            name='NoiseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='media')),
                ('label', models.CharField(default='test', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]