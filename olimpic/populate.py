from .models import Personal, Evento 
from django.http import HttpResponse
import csv

"""Script de preenchimento do banco de dados."""

class Number:
    
    def tratamento(self, valor):
        """Função que captura um dado numérico o Null proveniente 
           do arquivo csv.
        """
        enumero = valor.isnumeric()
        if enumero:
            return valor
        else:
            return None

info = Number()


def populate_db(request):
    """ Função para popular as tabelas do banco de dados"""
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
                                Height=info.tratamento(filas[4]), 
                                Weight=info.tratamento(filas[5]), 
                                Team=filas[6], 
                                NOC=filas[7]))

                events.append(Evento(Games=filas[8],
                            Age=info.tratamento(filas[3]), 
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