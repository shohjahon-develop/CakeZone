from django.db import models
from django.urls import reverse


# Create your models here.


class One(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Say(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    job = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Ved(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vedsDetail", args=[self.slug])

class Cust(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("custsDetail", args=[self.slug])



class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    bio = models.TextField()
    slug = models.SlugField(max_length=300)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chefsDetail", args=[self.slug])

















































































































































































