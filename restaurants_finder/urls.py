from django.urls import re_path,include
from . import views

urlpatterns = [

    re_path(r'^read_data/' , views.readData ,name= "readData"),
    re_path(r'^getrestaurants/' , views.GetRestaurants.as_view(), name="getrestaurants"),
    re_path(r'^home/',  views.showRestaurants , name = "home"),
    re_path(r'^showmap/', views.showmap , name="showmap"),
    re_path(r'^location/',views.GetLocation.as_view(), name="location")

]
