from re import I

from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serilizers import OrderSerilizer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.all(pk=id)
        if user.session_token == token:
            return True

    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"Error": "Please Re-login","code":"1"})
    
    if request.method=="POST":
        user_id = id
        transaction_id = request.POST["transaction_id"]
        product = request.POST["products"]
        amount = request.POST["amount"]

        total_products = len(product.split(',')[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
                return JsonResponse({"Error":"User Does Not Exists"})
        
        ordr = Order(user=user, product_name = product, total_products = total_pro, transaction_id = transaction_id, total_amount = amount)
        ordr.save()
        return JsonResponse({"Success":True, "Error":False, "Msg":"Order Placed Successfully"})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerilizer
