from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    comment = models.TextField()
    received  = models.DateTimeField(auto_now=False, auto_now_add = True)
    
    def __unicode__(self):
        return self.first_name+" "+self.last_name

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True) 
    updated =  models.DateTimeField(auto_now=True, auto_now_add = False)

