from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.

class Contacts(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    mobileNumber = models.CharField(max_length=10)

    class Meta:
        ordering = ['firstName']
