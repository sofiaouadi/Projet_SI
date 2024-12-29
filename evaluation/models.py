from django.db import models

# Create your models here.
from personnel.models import Personnel

class Evaluation(models.Model):
 dateEv= models.DateField
 score= models.FloatField(max_length=6) 
 commentaire= models.CharField(max_length=300)
