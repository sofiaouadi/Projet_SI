from django.db import models

# Create your models here.
from personnel.models import Personnel
class Salaire(models.Model):
 salaireBase= models.FloatField(max_length=12) 
 Prime= models.FloatField(max_length=12)
 heure_Sup= models.FloatField(max_length=12)
 avance= models.FloatField(max_length=12)
 jourAbsence= models.FloatField(max_length=2)
 salaireF = models.FloatField(max_length=12)
 SalaireEmp= models.ForeignKey(Personnel, on_delete=models.CASCADE)