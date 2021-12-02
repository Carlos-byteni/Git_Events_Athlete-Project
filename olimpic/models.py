from django.db import models
 

class Personal(models.Model):
    """ Criação do modelo Personal. class Personal herda 
        da classe models.Models sus funcionalidades.
        A classe Personal cria uma tabela em que seus atributos
        são as colunas da mesma. 
    """
    Name = models.CharField(max_length=255)
    Sex = models.CharField(max_length=1)
    Height = models.IntegerField(null=True, blank=True)
    Weight = models.IntegerField(null= True, blank=True)
    Team = models.CharField(max_length=255)
    NOC = models.CharField(max_length=255)
    
    def __str__(self):
        """ Método que imprime o objeto em um string.
        """
        return self.Name

class Evento(models.Model): 
    """Criação do modelo Evento.
    """

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







    
    
    
  