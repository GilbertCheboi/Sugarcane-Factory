from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Event(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="creator") 
   title = models.CharField(max_length=55, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   video = models.FileField(upload_to='videos/', blank=True, null=True)
   image = models.ImageField(upload_to='images/', blank=True, null=True)
   time = models.DateField(null=True)
   timestamp = models.DateTimeField(auto_now_add=True)

class Program(models.Model):
   name = models.CharField(max_length=255)
   start = models.DateField(null=True)
   end = models.DateField(null=True)
   products = models.CharField(max_length=255)
   