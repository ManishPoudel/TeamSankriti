'''from django.db import models
#from django.urls import re_path
#from .import views
from django.contrib.auth.models import User

# Create your models here.
# in django this class will automatically converted into the table of database
class Userview(models.Model):
  userid =models.IntegerField(primary_key=True)
  email = models.CharField(max_length=100)
  name= models.CharField(max_length=100)
  password = models.CharField(max_length=128)


class Reserveview(models.Model):
    starttime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reserveid = models.IntegerField()  # Assuming reserveid is an integer
    userid = models.IntegerField()     # Assuming userid is an integer
    parkingspaceid = models.IntegerField()  # Assuming parkingspaceid is an integer
'''

from django.db import models
from django.contrib.auth.models import User

class Userview(models.Model):
    userid = models.IntegerField(primary_key=True)
    
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

class Reserveview(models.Model):
    starttime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reserveid = models.IntegerField(primary_key=True)
    endtime = models.DateTimeField
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    parkingspaceid = models.IntegerField()

class Review(models.Model):
    reviewid = models.IntegerField(primary_key=True)  
    userid = models.ForeignKey(User, on_delete=models.CASCADE) 
    parkingid = models.CharField(max_length=50) 
    ratingid = models.IntegerField() 
    comment = models.TextField() 
    date = models.DateField()
#cd ApiProject
#ls
#pythorn manage.py runserver
class Parkingspace(models.Model):
   location = models.CharField(max_length=255)
   capacity = models.IntegerField()
   rate = models.DecimalField(max_digits=10, decimal_places=2)
   availability_status = models.BooleanField(default=True)
