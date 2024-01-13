from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ReserveViewSet, ReviewViewSet

# Create a router and register your viewsets with it.
router = DefaultRouter()
router.register(r'Userview', UserViewSet, basename='Userview')
router.register(r'Reserveview', ReserveViewSet, basename='Reserveview')
router.register(r'Review', ReviewViewSet, basename='Review')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('save/', include(router.urls)),
]