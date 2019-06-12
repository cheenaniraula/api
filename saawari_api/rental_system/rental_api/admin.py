from .models import Customer
from django.contrib import admin
from .models import VehicleCategory, Vehicle, Vehicle_Type, City, City_Place, Customer

# Register your models here.
admin.site.site_header = 'Sawaari'


class VehicleCategoryAdmin(admin.ModelAdmin):
    model = VehicleCategory
    list_display = ['name']
    search_fields = ('name',)


admin.site.register(VehicleCategory, VehicleCategoryAdmin)


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ['VehicleCategory', 'name', 'model', 'number_plate']
    search_fields = ('VehicleCategory', 'name', 'model', 'number_plate',)


admin.site.register(Vehicle, VehicleAdmin)


class Vehicle_TypeAdmin(admin.ModelAdmin):
    model = Vehicle_Type
    list_display = ['vehicle', 'fule_type',
                    'seat', 'image', 'perHrPrice', 'gear_type']
    search_fields = ('vehicle', 'fule_type', 'seat',)


admin.site.register(Vehicle_Type, Vehicle_TypeAdmin)


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name','city_image']
    search_fields = ('name',)


admin.site.register(City, CityAdmin,)


class City_PlaceAdmin(admin.ModelAdmin):
    model = City_Place
    list_display = ['city', 'place']
    search_fields = ('city', 'place',)


admin.site.register(City_Place, City_PlaceAdmin,)

# users/admin.py

# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomerCreationForm, CustomerChangeForm


# class CustomerAdmin(admin.ModelAdmin):
#     add_form = CustomerCreationForm
#     form = CustomerChangeForm
#     model = Customer
#     list_display = ['name', 'username', 'address', 'phone_number',
#                     'email', 'image', 'citizenship', 'licence']
#     search_fields = ('name', 'address', 'phone_number',
#                      'email', 'image', 'citizenship', 'licence',)

# admin.site.register(Customer, CustomerAdmin,)


class CustomerAdmin(admin.ModelAdmin):

    model = Customer
    list_display = ['name', 'address', 'phone_number',
                    'email', 'image', 'citizenship', 'licence']
    search_fields = ('name', 'address', 'phone_number',
                     'email', 'image', 'citizenship', 'licence',)


admin.site.register(Customer, CustomerAdmin,)
