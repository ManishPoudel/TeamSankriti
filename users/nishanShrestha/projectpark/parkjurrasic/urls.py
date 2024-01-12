from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingspaceViewset, UserViewSet, ReserveViewSet, ReviewViewSet#ParkingspaceViewSet

# Create a router and register your viewsets with it.
router = DefaultRouter()
router.register(r'Userview', UserViewSet, basename='Userview')
router.register(r'Reserveview', ReserveViewSet, basename='Reserveview')
router.register(r'Review', ReviewViewSet, basename='Review')
router.register(r'Parkingspace', ParkingspaceViewset, basename='parkingspace')

#router.register(r'Parkingspace', ParkingspaceViewSet, basename='Review')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
