from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Userview
from .models import Reserveview
from .models import Review
from .serializers import UserviewSerializer 
from .serializers import ReserveviewSerializer
from .serializers import ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Userview.objects.all()
    serializer_class = UserviewSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserveview.objects.all()
    serializer_class = ReserveviewSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer