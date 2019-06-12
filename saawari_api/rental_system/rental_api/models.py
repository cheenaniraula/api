from django.db import models as M
# from django.contrib.auth.models import AbstractUser

# Create your models here.


class VehicleCategory(M.Model):
    name = M.CharField(max_length=30)

    def __str__(self):
        return self.name


class Vehicle(M.Model):
    VehicleCategory = M.ForeignKey(
        VehicleCategory, related_name='vehicle', on_delete=M.CASCADE)
    name = M.CharField(max_length=30)
    model = M.CharField(max_length=30)
    number_plate = M.CharField(max_length=30)

    def __str__(self):
        return self.model


class Vehicle_Type(M.Model):
    vehicle = M.ForeignKey(Vehicle, related_name='fules', on_delete=M.CASCADE)
    fule_type = M.CharField(max_length=40)
    seat = M.IntegerField()
    gear_type = M.CharField(max_length=30)
    perHrPrice = M.IntegerField()
    image = M.ImageField(upload_to='vehicle/')

    def __str__(self):
        return self.vehicle.name


class City(M.Model):
    name = M.CharField(max_length=30)
    city_image = M.ImageField(upload_to='city/')

    def __str__(self):
        return self.name


class City_Place(M.Model):

    city = M.ForeignKey(City, related_name='cities', on_delete=M.CASCADE)
    place = M.CharField(max_length=30)

    def __str__(self):
        return self.place


# class Customer(AbstractUser):
#     name = M.CharField(max_length=30)
#     address = M.CharField(max_length=30)
#     phone_number = M.CharField(max_length=15)
#     # email = M.EmailField()
#     image = M.ImageField(upload_to='images/')
#     citizenship = M.ImageField(upload_to='citizenship/')
#     licence = M.ImageField(upload_to='licence/')

#     def __str__(self):
#         return self.email


class Customer(M.Model):
    name = M.CharField(max_length=30)
    address = M.CharField(max_length=30)
    phone_number = M.CharField(max_length=15)
    email = M.EmailField()
    image = M.ImageField(upload_to='images/')
    citizenship = M.ImageField(upload_to='citizenship/')
    licence = M.ImageField(upload_to='licence/')

    def __str__(self):
        return self.email
