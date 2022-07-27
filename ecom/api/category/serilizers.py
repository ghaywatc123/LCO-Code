
from unicodedata import name

from rest_framework import serializers
from .models import Category

class CategorySerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Category
        fields = ('name', 'description')