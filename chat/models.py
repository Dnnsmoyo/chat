# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    user =  models.OneToOneField('auth.User',null=True)
    photo = models.ImageField(upload_to='media')
    country = models.CharField(max_length=100)
    DOB = models.DateField()

    def __str__(self):
        return self.user.username