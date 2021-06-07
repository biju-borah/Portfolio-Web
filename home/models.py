import django
from django.db import models
from datetime import date

# Create your models here.

class Project(models.Model):
    '''
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()

    '''

    name = models.CharField(max_length=50,null=True)
    language = models.TextField(max_length=50,null=True)
    desc = models.TextField()
    url = models.CharField(max_length=50,null=True)
    month = models.TextField(max_length=10,null=True)


class Message(models.Model):
    email = models.CharField(max_length=100)
    message = models.TextField()

