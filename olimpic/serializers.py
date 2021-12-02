
from rest_framework import serializers
from .models import Personal, Evento


class PersonalSerializer(serializers.ModelSerializer):
    """Serializador do modelo Personal.
    """
    class Meta:
        model = Personal
        fields = '__all__'

#Serializador do modelo Evento
class EventoSerializer(serializers.ModelSerializer):
    """Serializador do modelo Evento.
    """
    class Meta:
        model = Evento
        fields = '__all__'




