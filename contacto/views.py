from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import status
from .models import Contacto
from .serializers import ContactoSerializer

# Create your views here.

class ContactoViewSet(viewsets.ModelViewSet):
    authenticated_users_only = False
    permission_classes = [AllowAny]
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()

    def update(self, request, *args, **kwargs):
        contacto = Contacto.objects.get()
        data = request.data
        contacto.nombre = data['nombre']
        contacto.apellido = data['apellido']
        contacto.fono = data['fono']
        contacto.email = data['email']
        contacto.fecha_nac = data['fecha_nac']
        contacto.save()
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)
    
    """ 
    def partial_update(self, request, pk=None):
        #Handles updating part of an object

        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        #Handle removing an object

        return Response({'http_method': 'DELETE'})
    """