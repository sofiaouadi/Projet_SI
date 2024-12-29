from django.db import models

# Create your models here.
from recrutement.models import recrutement
class candidat(models.Model):
 nom= models.CharField(max_length=50)
 prenom= models.CharField(max_length=50)
 numT= models.FloatField(max_length=12) 
 emeil = models.CharField
 statutCondidat = models.CharField
 recrutementCandidat = models.ForeignKey(recrutement, on_delete=models.CASCADE)