from rest_framework import serializers
from .models import VehicleCategory,Vehicle,Vehicle_Type,City,City_Place,Customer

class VehicleCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = '__all__'


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'




class Vehicle_TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Type
        fields = '__all__'



class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class City_PlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = City_Place
        fields = '__all__'



class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'



