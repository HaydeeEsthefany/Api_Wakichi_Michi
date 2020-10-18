# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import ArrayField



class User(models.Model):
  
    fullname        = models.CharField(max_length=100, null=False)
    email           = models.CharField(max_length=200, null=False)
    username        = models.CharField(max_length=200, null=False)
    since           = models.DateTimeField()
    weeks           = models.IntegerField()  
    adult           = models.IntegerField()
    children        = models.IntegerField()  
    dir_ip          = models.CharField(max_length=15)
    is_active       = models.BooleanField(null=True,  default=True)
    state_value     = models.IntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(null=True)
    

    last_login = None
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta: db_table = "user"

