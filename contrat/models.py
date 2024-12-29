from django.db import models

# Create your models here.
from personnel.models import Personnel

class Contrat(models.Model):
 type= models.CharField(max_length=3)
 dateD= models.DateField
 dateF= models.DateField
 salaire= models.FloatField(max_length=12) 
 contratEmp= models.ForeignKey(Personnel, on_delete=models.CASCADE)