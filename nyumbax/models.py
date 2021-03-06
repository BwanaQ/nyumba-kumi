from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models import Count

# Create your models here.


class Hood(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    admin = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def all_users(request):
        members = Hood.objects.anotate(number_of_members=Count('user'))
        return number_of_members


class Business(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=100)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "businesses"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Essential(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    officer = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
