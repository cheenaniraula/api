from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.




class Vehicle_CategoryView(generics.ListCreateAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializers




class VehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializers
    



class Vehicle_TypeView(generics.ListCreateAPIView):
    queryset = Vehicle_Type.objects.all()
    serializer_class = Vehicle_TypeSerializers



class CityView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers




class City_PlaceView(generics.ListCreateAPIView):
    queryset = City_Place.objects.all()
    serializer_class = City_PlaceSerializers




class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    

