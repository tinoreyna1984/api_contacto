from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacto
from .serializers import ContactoSerializer

# Create your views here.

class ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
