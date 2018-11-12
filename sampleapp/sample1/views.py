from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import Foo
import json
from django.http import JsonResponse
# Create your views here.

@require_GET
def index(request):
    return JsonResponse({'a':1, 'b': 2})

@require_GET
def hi(request, name, old):
    return JsonResponse({'name': name, 'old': old})

@require_GET
def hello(request):
    name = request.GET.get('name')
    return JsonResponse({'message': 'hello %s' % name })


@require_POST
@csrf_exempt
def body(request):
    b = request.body.decode('utf-8')
    json_body = json.loads(b)
    a = json_body['a']
    b = json_body['b']
    return JsonResponse({
        'a': a + 1,
        'b': b + 1,
    })

@require_GET
def ping(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
        result = cursor.fetchone()[0]

    return JsonResponse({
        'result': 'pong' if result == 1 else 'failed',
    })

@require_GET
def getFooList(request):
    qs = Foo.objects.all()
    qs_json = serializers.serialize('json', qs)
    return JsonResponse({
        "foos": Foo.object.all()
    });
