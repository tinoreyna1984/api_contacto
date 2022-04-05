from dataclasses import fields
from rest_framework import serializers

# Here we can serialize the models created previously
from .models import Contacto

# Define a serializer class

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'
