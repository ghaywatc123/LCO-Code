from rest_framework import viewsets

from .serilizers import CategorySerilizers

from .models import Category
from . import serilizers



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerilizers




