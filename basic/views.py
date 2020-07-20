from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pra
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializer import PraSerializer
from rest_framework import viewsets
# Create your views here.

@csrf_exempt
def pra(request):
    if request.method == 'GET':
        pra = Pra.objects.all()
        serializer = PraSerializer(pra, many =True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PraSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)
    return HttpResponse('Welcome')

# class PraSet(viewsets.ModelViewSet):
#     queryset  = Pra.objects.all()
#     serializer_class = PraSerializer

