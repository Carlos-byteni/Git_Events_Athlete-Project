
#Importação de pacotes de operação
from django.shortcuts import render
from .models import Personal, Evento 
from .serializers import PersonalSerializer, EventoSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv


#Criação da classe do tipo ViewSet
#Esta classe fornece a lista do pessoal esportivo:

#---------------------Personal-------------------------

class PersonalViewSet(viewsets.ViewSet):

    # Lista das instânicias do bando de dados(baseado no método GET de HTTP)
    def list(self, request):
        queryset = Personal.objects.all()
        serializer = PersonalSerializer(queryset, many=True)
        return Response(serializer.data)
    # Retrieve das instâncias do banco de dados(baseado no método GET de HTTP)
    def retrieve(self,request, pk=None):
        queryset = Personal.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonalSerializer(person)
        return Response(serializer.data)

# Criação da classe Viewset herdando de ModelViewSet. Esta clase é combinada com
# a classe: PersonalViewSet(viewsets.ViewSet) para completmentar a operação com ModelViewSet.
# ModelViewSet permite obter as ações: create, patch, put, destroy de forma intrínseca

class PersonalViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()
    serializer = PersonalSerializer(queryset, many=True)
     

#-------------------- Eventos-------------------------

#Criação da classe do tipo ViewSet
#Esta classe fornece a lista do pessoal esportivo:

class EventoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Evento.objects.all()
        serializer = EventoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request, pk=None):
        queryset = Evento.objects.all()
        evento = get_object_or_404(queryset, pk=pk)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    serializer = EventoSerializer(queryset, many=True)



# Função que retorna valor númerico o un valo NUll
def tratamento(valor):
    enumero = valor.isnumeric()
    if enumero:
        return valor
    else:
        return None


#sequência de população do banco de dados:
def populate_db(request):
    persons = []
    events = []

    # É aberto o respectivo arquivo em formato csv     
    with open('athlete_events.csv','r') as information:
        data = list(csv.reader(information, delimiter=','))
    
    # Script para obter a informação das linhas do arquivo
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
    
    # Preenchimento dos dados no banco de dados           
    if len(persons)>0: 
        Personal.objects.bulk_create(persons)
        Evento.objects.bulk_create(events)
    return HttpResponse('it is done!')



    




