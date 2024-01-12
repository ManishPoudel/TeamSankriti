'''from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Userview
from .serializers import UserviewSerializer

class userApiview(APIView):
  serializer_class = UserviewSerializer
  def get(self,request):
# django will automatically converted from this statement in sql form 
   alluser = Userview.objects.all().values()
   return Response({"Messages":"list of users","list users":alluser}) 
  def get(self,request):
   print("request dat is:",request.data)
   serializer_o = UserviewSerializer(data= request.data)
# we got from the input parameter request and
   if (serializer_o.is_valid()):
    userApiview.objects.create(userid= request.data['userid'],email = request.data['email'],name = request.data['name'],password = request.data['password'])

   auser = userApiview.objects.all().filter(userid = request.data['userid']).values()
   return Response({"Messages":"new user added!","users":auser})'''



        

'''from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Userview
from .models import Reserveview
from .serializers import UserviewSerializer
from .serializers import ReserveviewSerializer

class userApiview(APIView):
    serializer_class = UserviewSerializer

    def get(self, request):
        # Query the Userview model, not the userApiview
        alluser = Userview.objects.all().values()
        return Response({"Messages": "List of users", "List users": alluser})

    def post(self, request):
        print("Request data is:", request.data)
        serializer_o = UserviewSerializer(data=request.data)

        if serializer_o.is_valid():
            Userview.objects.create(userid=request.data['userid'], email=request.data['email'], name=request.data['name'], password=request.data['password'])

            # Again, query the Userview model
            auser = Userview.objects.filter(userid=request.data['userid']).values()
            return Response({"Messages": "New user added!", "Users": auser})

class ReserveViewSet(viewsets.ModelViewSet):
                                         
   queryset = Reserveview.objects.all()
   serializer_class = ReserveviewSerializer
'''

'''from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Userview, Reserveview
from .serializers import UserviewSerializer 
from .serializers import ReserveviewSerializer

class userApiview(APIView):
    serializer_class = UserviewSerializer

    def get(self, request):
        all_users = Userview.objects.all().values()
        return Response({"message": "List of users", "users": all_users})

    def post(self, request):
        serializer = UserviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New user added!", "user": serializer.data})
        return Response({"message": "Invalid data"})

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserveview.objects.all()
    serializer_class = ReserveviewSerializer
'''
# ApiApplication/views.py

#from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Userview
from .models import Reserveview
from .models import Review
from .models import Parkingspace
from .serializers import UserviewSerializer 
from .serializers import ReserveviewSerializer
from .serializers import ReviewSerializer
from .serializers import Parkingspaceserializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Userview.objects.all()
    serializer_class = UserviewSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserveview.objects.all()
    serializer_class = ReserveviewSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class ParkingspaceViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = Parkingspaceserializer