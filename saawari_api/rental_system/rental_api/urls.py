from django.urls import path
from .views import *


app_name = "rental_api"


urlpatterns = [
    path('vehic_cat/', Vehicle_CategoryView.as_view(), name = 'vehicle-category'),
    path('vehicle/', VehicleView.as_view(), name = 'vehicle'),
    path('vehic_type/', Vehicle_TypeView.as_view(), name = 'vehicle-type'),
    path('city/', CityView.as_view(), name = 'city'),
    path('city_place/', City_PlaceView.as_view(), name = 'city-place'),
    path('customer/', CustomerView.as_view(),name = 'customer'),
   
   ]