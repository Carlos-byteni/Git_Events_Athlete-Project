from .models import Personal, Evento 
from .serializers import PersonalSerializer, EventoSerializer
from rest_framework.response import Response
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404




#Criação da classe do tipo ViewSet
#Esta classe fornece a lista do pessoal esportivo:

#_____________Personal_____________________

class PersonalViewSet(viewsets.ViewSet):
    """A classe PersoalViewSet herda viewsets de classe ViewSet.
    """

    
    def list(self, request):
        """Método que lista as instâncias do modelo Personal.
           Este método é baseado nos métodos GET de HTTP.
        """
        queryset = Personal.objects.all()
        serializer = PersonalSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request, pk=None):
        """Recuperação das instâncias do banco de dados.
           Este método também é baseado em GET de HTTP.
        """
        queryset = Personal.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonalSerializer(person)
        return Response(serializer.data)


class PersonalViewSet(viewsets.ModelViewSet):
    """Criação da classe Viewset herdando de ModelViewSet. 
       ModelViewSet permite obter as ações: create, patch, put, destroy de forma intrínseca.
    """
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()
    serializer = PersonalSerializer(queryset, many=True)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Name', 'Team', 'NOC',)
     

#_____________Eventos_____________________

class EventoViewSet(viewsets.ViewSet):
    """É criada uma classe do tipo ViewSet
       Essa classe fornece a lista da competição esportiva.
    """
    def list(self, request):
        """ Método utilizado para listar os eventos esportivos.
            Esta listagem é feita ao obter as instâncias do queryset.
        """
        queryset = Evento.objects.all()
        serializer = EventoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request, pk=None):
        """ Os dados dos eventos são recuperados baseado no método GET HTTP.
        """
        queryset = Evento.objects.all()
        evento = get_object_or_404(queryset, pk=pk)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

class EventoViewSet(viewsets.ModelViewSet):
    """Criação da classe Viewset herdando de ModelViewSet. 
       Esta clase é complementada com a classe EventoViewSet(viewsets.ViewSet) 
    """                                                                                               
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    serializer = EventoSerializer(queryset, many=True)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Games', 'Year', 'Event',)





    




