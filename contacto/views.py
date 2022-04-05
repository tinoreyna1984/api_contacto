from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Contacto
from .serializers import ContactoSerializer

# Create your views here.

class ContactoViewSet(viewsets.ModelViewSet):
    authenticated_users_only = False
    permission_classes = [AllowAny]
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()
