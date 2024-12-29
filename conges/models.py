from django.db import models

# Create your models here.
from personnel.models import Personnel

class conges(models.Model):
 type= models.CharField(max_length=50)
 dateD= models.DateField
 dateF= models.DateField
 Empconge = models.ForeignKey(Personnel, on_delete=models.CASCADE)