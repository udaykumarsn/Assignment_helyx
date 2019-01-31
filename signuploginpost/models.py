from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Registration(models.Model):
    email_id = models.TextField(null=True)
    name= models.CharField(max_length=250, null=True)