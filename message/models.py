from django.db import models

# Create your models here.


class InputMessage(models.Model):

    name = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
