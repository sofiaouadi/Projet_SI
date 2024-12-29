from django.db import models

# Create your models here.
from service.models import service
#from recrutement.models import recrutement

class Personnel(models.Model):
 nom= models.CharField(max_length=50)
 prenom= models.CharField(max_length=50)
 dateN= models.DateField
 numT= models.FloatField(max_length=12) 
 email = models.CharField
 posteOccupe = models.CharField(max_length=50)
 dateEmbauche = models.DateField
 adresse = models.TextField 
 serviceEmp = models.ForeignKey(service, on_delete=models.CASCADE) 
 #Embauchement = models.ForeignKey(recrutement.recrutement, on_delete=models.CASCADE)