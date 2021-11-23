
from rest_framework import serializers
from .models import Personal, Evento

#Serializador do modelo Personal
class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

#Serializador do modelo Evento
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'




