"""
URL configuration for ApiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


    
"""
'''from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ApiApplication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url("Userview/",views.UserApiview.as_view())
]'''


'''from django.contrib import admin
from django.urls import path, re_path
from ApiApplication.views import userApiview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Userview/', views.UserApiview.as_view()),
    # OR using path (if you don't need a regex pattern):
    # path('userview/', views.UserApiview.as_view()),
]'''

'''from django.contrib import admin
from django.urls import path
from ApiApplication import views
from ApiApplication.views import userApiview 
from ApiApplication.views import  ReserveApiView 
# Correctly imported
from rest_framework import routers
router = routers.DefaultRouter()
router.register('Reserveview/',views.ReserveViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Userview/', userApiview.as_view()),
    #path('Reserveview/',ReserveApiView.as_view()),
      # Correctly referenced
    # OR using path (if you don't need a regex pattern):
    # path('userview/', userApiview.as_view()),
]'''

'''from django.contrib import admin
from django.urls import path, include
from ApiApplication.views import UserViewSet
from ApiApplication.views import ReserveViewSet

# Correctly imported
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'userview', UserViewSet, basename='userview')
router.register(r'reserveview', ReserveViewSet, basename='reserveview')
router.register(r'review', ReserveViewSet, basename='review')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('reserveview/', include(router.urls)),
    path('review/',include(router.urls))
]'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ApiApplication.urls')),  # replace 'yourapp' with your actual app name
]

