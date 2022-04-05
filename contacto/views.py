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

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
