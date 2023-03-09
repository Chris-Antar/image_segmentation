from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import math, datetime as dt
from django.utils import timezone




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length = 12)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    

    def __str__(self):
        return f'{self.user.username} Profile'

class MultipleImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.FileField(upload_to='media')
    label = models.CharField(max_length = 100, default = "test")
    segmented = models.BooleanField(default = False)


class NoiseImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.FileField()
    label = models.CharField(max_length = 100, default = "test")
    segmented = models.BooleanField(default = False)
