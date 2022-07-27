from unicodedata import category
from django import urls, views
from django.urls import path, include

from rest_framework import authtoken
from . views import home


urlpatterns = [
    path('',home, name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
    path('order/',include('api.order.urls')),
    path('payment/',include('api.payment.urls'))
    #api.orderpath('api-token-auth/',views.obtain_auth_token, name='api_token_auth')

]