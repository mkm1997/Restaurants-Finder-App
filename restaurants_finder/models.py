from django.db import models

# Create your models here.

class Restaurants(models.Model):
    restaurant_id = models.CharField(max_length=200,unique=True)
    restaurant_name = models.CharField(max_length=500)
    cuisines = models.CharField(max_length=2000)
    avg_cost_for_two = models.IntegerField()
    currency  = models.CharField(max_length=500)
    has_table_booking = models.CharField(max_length=100)
    has_online_booking = models.CharField(max_length=100)
    agg_rating = models.IntegerField()
    rating_color = models.CharField(max_length=1000)
    rating_text = models.CharField(max_length=2000)
    votes = models.IntegerField()
    def __str__(self):
        return self.restaurant_name

class RestaurantsLocation(models.Model):
    restaurant_id = models.OneToOneField(Restaurants,on_delete=models.CASCADE,related_name="restaurants")
    country_code = models.CharField(max_length=100)
    city = models.CharField(max_length=1000)
    address = models.CharField(max_length=2000)
    locality = models.CharField(max_length=2000)
    locality_verb = models.CharField(max_length=2000)
    longitude = models.CharField(max_length=500)
    latitude = models.CharField(max_length=500)

    def __str__(self):
        return self.restaurant_id.restaurant_name
