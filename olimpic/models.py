
from django.db import models

#Criação dos modelos a serem usados


class Personal(models.Model):
    Name = models.CharField(max_length=255)
    Sex = models.CharField(max_length=1)
    Height = models.IntegerField(null=True, blank=True)
    Weight = models.IntegerField(null= True, blank=True)
    Team = models.CharField(max_length=255)
    NOC = models.CharField(max_length=255)


    
    def __str__(self):
        return self.Name

class Evento(models.Model): 
    Games = models.CharField(max_length=255)
    Age = models.IntegerField(null=True, blank=True)
    Year = models.PositiveIntegerField()
    Season = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Sport = models.CharField(max_length=255) 
    Event = models.CharField(max_length=255)
    Medal = models.CharField(max_length=255)
    personal = models.ManyToManyField(Personal)
    
    def __str__(self):
        return self.Games







    
    
    
  