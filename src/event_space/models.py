from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    received  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.first_name + self.last_name
