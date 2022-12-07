
from rest_framework import serializers

from .models import Order

class OrderSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'