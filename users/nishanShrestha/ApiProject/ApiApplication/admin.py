
# parkjurrasic/admin.py
from django.contrib import admin
from .models import Review, Userview, Reserveview, Parkingspace

admin.site.register(Userview)
admin.site.register(Reserveview)
admin.site.register(Review)
admin.site.register(Parkingspace)