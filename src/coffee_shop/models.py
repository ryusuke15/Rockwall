from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Mailing_List(models.Model):
    email = models.EmailField(max_length=200, blank=True)
    received  = models.DateTimeField(auto_now=False, auto_now_add = True)
    
    def __unicode__(self):
        return self.email
