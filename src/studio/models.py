from __future__ import unicode_literals
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

def tenant_image_location(instance, filename):
    return "studio/tenant/%s/%s" %(instance.room, filename)

def blog_image_location(instance, filename):
    return "studio/blog/%s/%s" %(instance.date, filename)

def room_image_location(instance, filename):
    return "studio/room/%s/%s" %(instance.room, filename)

class Tenant(models.Model):

    ROOM_NUMBERS_CHOICES = (
    
    ('A01','A01'),('A02','A02'),('A03','A03'),('A04','A04'),('A05','A05'),('A06','A06'),('A07','A07'),('A08','A08'),
    ('A09','A09'),('A10','A10'),('A11','A11'),('A12','A12'),('A13','A13'),('A14','A14'),('A15','A15'),('A16','A16'),
    ('A17','A17'),('A18','A18'),('A19','A19'),('A20','A20'),('A21','A21'),('A22','A22'),('A23','A23'),('A24','A24'),
    ('A25','A25'),('A26','A26'),('A27','A27'),('A28','A28'),('A29','A29'),('A30','A30'),('A31','A31'),('A32','A32'),
    ('A33','A33'),('A34','A34'),('A35','A35'),('A36','A36'),('A37','A37'),('A38','A38'),

    ('B01','B01'),('B02','B02'),('B03','B03'),('B04','B04'),('B05','B05'),('B06','B06'),('B07','B07'),('B08','B08'),
    ('B09','B09'),('B10','B10'),('B11','B11'),('B12','B12'),('B13','B13'),('B14','B14'),('B15','B15'),('B16','B16'),
    ('B17','B17'),('B18','B18'),('B19','B19'),('B20','B20'),('B21','B21'),('B22','B22'),('B23','B23'),('B24','B24'),
    ('B25','B25'),('B26','B26'),('B27','B27'),('B28','B28'),('B29','B29'),('B30','B30'),('B31','B31'),('B32','B32'),
    ('B33','B33'),('B34','B34'),('B35','B35'),('B36','B36'),('B37','B37'),('B38','B38'),

    ('C01','C01'),('C02','C02'),('C03','C03'),('C04','C04'),('C05','C05'),('C06','C06'),('C07','C07'),('C08','C08'),
    ('C09','C09'),('C10','C10'),('C11','C11'),('C12','C12'),('C13','C13'),('C14','C14'),('C15','C15'),('C16','C16'),
    ('C17','C17'),('C18','C18'),('C19','C19'),('C20','C20'),('C21','C21'),('C22','C22'),('C23','C23'),('C24','C24'),
    ('C25','C25'),('C26','C26'),('C27','C27'),('C28','C28'),('C29','C29'),('C30','C30'),('C31','C31'),('C32','C32'),
    ('C33','C33'),('C34','C34'),('C35','C35'),('C36','C36'),('C37','C37'),('C38','C38'),

    ('D01','D01'),('D02','D02'),('D03','D03'),('D04','D04'),('D05','D05'),('D06','D06'),('D07','D07'),('D08','D08'),
    ('D09','D09')
    )

    first_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length = 100)    
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to=tenant_image_location,  null=True, blank=True)
    room = models.CharField(max_length=30, choices=ROOM_NUMBERS_CHOICES, unique=True)
    content = models.TextField(max_length= 400)
    web = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True) 
    facebook = models.URLField(null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name +" "+ self.last_name

class Contact(models.Model):
    first_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=50)
    date = models.DateField()
    message = models.TextField()
    received  = models.DateTimeField(auto_now=False, auto_now_add = True)
    
    def __unicode__(self):
        return self.first_name +" "+ self.last_name

class Coworking_Space(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    received  = models.DateTimeField(auto_now=False, auto_now_add = True)
    
    def __unicode__(self):
        return self.first_name +" "+ self.last_name

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=blog_image_location, null=True, blank=True)
    youtube_link = models.URLField(null=True,blank=True)
    date = models.DateField()
    spotlight = models.BooleanField(default=False)
    upcoming = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True) 
    updated =  models.DateTimeField(auto_now=True, auto_now_add = False)
   
    def clean(self):
        if self.image and self.youtube_link:
            raise ValidationError("Uploading both videos and photos are prohibitted.")

class Mailing_list(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)   

class Room(models.Model):

    ROOM_NUMBERS_CHOICES = (
    
    ('A01','A01'),('A02','A02'),('A03','A03'),('A04','A04'),('A05','A05'),('A06','A06'),('A07','A07'),('A08','A08'),
    ('A09','A09'),('A10','A10'),('A11','A11'),('A12','A12'),('A13','A13'),('A14','A14'),('A15','A15'),('A16','A16'),
    ('A17','A17'),('A18','A18'),('A19','A19'),('A20','A20'),('A21','A21'),('A22','A22'),('A23','A23'),('A24','A24'),
    ('A25','A25'),('A26','A26'),('A27','A27'),('A28','A28'),('A29','A29'),('A30','A30'),('A31','A31'),('A32','A32'),
    ('A33','A33'),('A34','A34'),('A35','A35'),('A36','A36'),('A37','A37'),('A38','A38'),

    ('B01','B01'),('B02','B02'),('B03','B03'),('B04','B04'),('B05','B05'),('B06','B06'),('B07','B07'),('B08','B08'),
    ('B09','B09'),('B10','B10'),('B11','B11'),('B12','B12'),('B13','B13'),('B14','B14'),('B15','B15'),('B16','B16'),
    ('B17','B17'),('B18','B18'),('B19','B19'),('B20','B20'),('B21','B21'),('B22','B22'),('B23','B23'),('B24','B24'),
    ('B25','B25'),('B26','B26'),('B27','B27'),('B28','B28'),('B29','B29'),('B30','B30'),('B31','B31'),('B32','B32'),
    ('B33','B33'),('B34','B34'),('B35','B35'),('B36','B36'),('B37','B37'),('B38','B38'),

    ('C01','C01'),('C02','C02'),('C03','C03'),('C04','C04'),('C05','C05'),('C06','C06'),('C07','C07'),('C08','C08'),
    ('C09','C09'),('C10','C10'),('C11','C11'),('C12','C12'),('C13','C13'),('C14','C14'),('C15','C15'),('C16','C16'),
    ('C17','C17'),('C18','C18'),('C19','C19'),('C20','C20'),('C21','C21'),('C22','C22'),('C23','C23'),('C24','C24'),
    ('C25','C25'),('C26','C26'),('C27','C27'),('C28','C28'),('C29','C29'),('C30','C30'),('C31','C31'),('C32','C32'),
    ('C33','C33'),('C34','C34'),('C35','C35'),('C36','C36'),('C37','C37'),('C38','C38'),

    ('D01','D01'),('D02','D02'),('D03','D03'),('D04','D04'),('D05','D05'),('D06','D06'),('D07','D07'),('D08','D08'),
    ('D09','D09')
    )

    room = models.CharField(max_length=30, choices=ROOM_NUMBERS_CHOICES, unique=True)
    size = models.IntegerField()
    rent = models.IntegerField()
    image = models.ImageField(upload_to=room_image_location)
    content = models.TextField(max_length=140)
