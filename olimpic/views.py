from .models import Personal, Evento 
from .serializers import PersonalSerializer, EventoSerializer
from rest_framework.response import Response
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv


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
    """Criação da classe Viewset herdando de ModelViewSet. Esta clase é combinada com
    a classe PersonalViewSet(viewsets.ViewSet) para completmentar a operação com ModelViewSet.
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
       Esta clase é complementada com a classe EventoViewSet(viewsets.ViewSet) para 
       operar com ModelViewSet
    """                                                                                               
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    serializer = EventoSerializer(queryset, many=True)


# Script de preenchimento do banco de dados
# Função que retorna valor númerico o un valor NUll

def tratamento(valor):
    """Função que captura um dado proveniente 
       do arquivo csv. 
       Se o valor for númerico retorna um valor numérico.
       Se o valor for string retorna um Null.
    """
    enumero = valor.isnumeric()
    if enumero:
        return valor
    else:
        return None

def populate_db(request):
    """ Função para popular as tabelas do banco de dados.
        persons = [], serve para armazenar os dados dos atletas
        events = [], serve para armazenar os dados dos eventos esportivos.
        Dentro desta função é carregado e lido o arquivo csv.
        A variável data capta uma lista dos dados do arquivo csv.
        É feita uma iteração baseada nos id dos atletas. 
        Após disso são adicionados os dados dos atletas e dos eventos nos 
        campos do modelo.
        Finalmente, é usado um bulk_create para crear as instâncias dos objetos dentro da 
        tabela do bando de dados.
    """
    persons = []
    events = []
     
    with open('athlete_events.csv','r') as information:
        data = list(csv.reader(information, delimiter=','))
    
        last_id = 0 
        for filas in data[1:]:
            
            if int(filas[0])>last_id:
                last_id = int(filas[0])
                persons.append(Personal(Name=filas[1], 
                                    Sex=filas[2], 
                                    Height=tratamento(filas[4]), 
                                    Weight=tratamento(filas[5]), 
                                    Team=filas[6], 
                                    NOC=filas[7]))

                events.append(Evento(Games=filas[8],
                                Age=tratamento(filas[3]), 
                                Year=filas[9], 
                                Season=filas[10], 
                                City=filas[11], 
                                Sport=filas[12],
                                Event=filas[13],
                                Medal=filas[14]))         
    if len(persons)>0: 
        Personal.objects.bulk_create(persons)
        Evento.objects.bulk_create(events)
    return HttpResponse('it is done!')



    




