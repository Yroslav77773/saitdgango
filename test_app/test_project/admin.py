from django.contrib import admin
from .models import Car, CarImage, CarReview

admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(CarReview)