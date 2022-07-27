from urllib import request
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return JsonResponse({'Name':'Chetan', 'info':"I am Here"})
