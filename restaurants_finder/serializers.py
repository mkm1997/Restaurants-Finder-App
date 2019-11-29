from rest_framework.serializers import ModelSerializer,Serializer
from .models import Restaurants , RestaurantsLocation

class RestaurantSerializers(ModelSerializer):
    class Meta:
        model = Restaurants
        depth = 1
        fields = '__all__'


class RestaurantsLocationSerializers(ModelSerializer):
    # restauranst_id  = RestaurantSerializers()

    class Meta:
        model = RestaurantsLocation
        fields = '__all__'