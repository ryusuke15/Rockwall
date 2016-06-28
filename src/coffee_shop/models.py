from __future__ import unicode_literals
from django.db import models

# Create your models here.

def blog_image_location(instance, filename):
    return "brew/%s/%s" %(instance.id, filename)

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
    image = models.ImageField(upload_to=blog_image_location, 
                            null=True, 
                            blank=True, 
                            width_field="width_field", 
                            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True) 
    updated =  models.DateTimeField(auto_now=True, auto_now_add = False)

class Mailing_list(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)   
