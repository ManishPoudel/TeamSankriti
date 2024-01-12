'''from rest_framework import serializers
from .models import  Userview 
from .models import Reserveview

class UserviewSerializer(serializers.ModelSerializer):
    # class Meta:
      model = Userview
      userid =serializers.IntegerField(label = "enter the user id")
      email = serializers.CharField(label = "enter the email")
      name= serializers.CharField(label = "enter the name")
      password = serializers.CharField(label = "enter the password")

class ReserveviewSerializer(serializers.ModelSerializer):
   class Meta:
     model= Reserveview
     fields = "__all__" 
'''


'''starttime = serializers.IntegerField(label="Enter the start time")
     price = serializers.FloatField(label="Enter the price")
     reserveid = serializers.IntegerField(label="Enter the reserve ID")
     userid = serializers.IntegerField(label="Enter the user ID")
     parkingspaceid = serializers.IntegerField(label="Enter the parking space ID")'''



'''from rest_framework import serializers
from .models import Userview 

class UserviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userview
        fields = ['userid', 'email', 'name', 'password']'''


from rest_framework import serializers
from .models import Userview
from .models import  Reserveview
from .models import Review
from .models import Parkingspace


class UserviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userview
        fields = "__all__"

class ReserveviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserveview
        fields = "__all__"
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
       model = Review
       fields = "__all__"
    
class Parkingspaceserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"