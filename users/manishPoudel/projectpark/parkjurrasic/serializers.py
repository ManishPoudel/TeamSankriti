from rest_framework import serializers
from .models import Userview
from .models import  Reserveview
from .models import Review


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