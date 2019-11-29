from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RestaurantsLocation,Restaurants
from .serializers import RestaurantsLocationSerializers ,RestaurantSerializers
from django.http import  HttpResponse
import csv

# Create your views here.

li = []
for i in Restaurants.objects.all():
    for j in i.cuisines.split(','):
        if j.strip() not in li:
            li.append(j.strip())

print(li)


def read_csv_file():
    rows = []
    with open("/home/manish/PycharmProjects/smartQI/Restaurants/restaurantsa9126b3.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    count = 0
    for row in rows:
        if count >0:
            Restaurants.objects.create(restaurant_id = row[0], restaurant_name = row[1],  cuisines= row[2],
                                       avg_cost_for_two = row[3] ,currency= row[4] , has_table_booking = row[5],
                                       has_online_booking = row[6],
                                       agg_rating = row[7], rating_text = row[9] , rating_color= row[8],votes = row[10])
        count = count+1
    return


def read_csv_Location():
    rows = []
    with open("/home/manish/PycharmProjects/smartQI/Restaurants/restaurant_addc9a1430.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    count = 0
    for row in rows:
        if count >0:
            RestaurantsLocation.objects.create(restaurant_id = Restaurants.objects.get(restaurant_id =row[0]), country_code = row[1] , city = row[2],
                                               address = row[3], locality = row[4], locality_verb = row[5] ,
                                               longitude = row[6] , latitude = row[7])
        count = count+1
    return

def readData(request):
    read_csv_file()
    read_csv_Location()

    return HttpResponse("data is added")




class GetLocation(generics.ListAPIView):

    serializer_class = RestaurantsLocationSerializers

    def get(self, request, *args, **kwargs):
        get_response = super().get(request, *args, **kwargs)
        return get_response

    def get_queryset(self):
        restaurant_id = self.request.query_params["id"]
        print(restaurant_id)
        queryset = RestaurantsLocation.objects.filter(restaurant_id=Restaurants.objects.get(restaurant_id = restaurant_id))
        return queryset



class GetRestaurants(generics.ListAPIView):

    serializer_class = RestaurantSerializers

    def get(self, request, *args, **kwargs):
        get_response = super().get(request, *args, **kwargs)
        return get_response

    def get_queryset(self):
        try:

            qp = self.request.query_params["name"]
            print("houu")
            srt = self.request.query_params["sort"]
            print("houu2")
            cuisine= self.request.query_params["cuisine"]
            print("houu3")
            print(cuisine)
            queryset = Restaurants.objects.filter(cuisines__contains = cuisine,restaurant_name__contains = qp).order_by(srt)
            print(queryset)
            for i in cuisine.split(','):
                queryset = queryset.objects.filter(cuisines=i)


            return queryset
        except:
            queryset = Restaurants.objects.all()
            return queryset








def showRestaurants(request):

    return render(request,'restaurant_list.html' , {"cuisines":li})

def showmap(request):

    return render(request,'restaurant_location.html')




