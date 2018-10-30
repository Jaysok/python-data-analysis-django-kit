from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    return JsonResponse({'a':1, 'b': 2})