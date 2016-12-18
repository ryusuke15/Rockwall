from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

def blog_image_location(instance, filename):
    return "project_space/%s/%s" %(instance.date, filename)

class Contact(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()
    received  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.first_name +" "+ self.last_name

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=blog_image_location,
                        null=True, 
                        blank=True) 
    youtube_link = models.URLField(null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()
    recent = models.BooleanField(default=False)
    upcoming = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True) 
    updated = models.DateTimeField(auto_now=True, auto_now_add = False)

    def clean(self):
        if self.image and self.youtube_link:
            raise ValidationError("Uploading both videos and photos are prohibitted.")


class Mailing_list(models.Model):
    email = models.EmailField()
    timestamp  = models.DateTimeField(auto_now=False, auto_now_add=True)


