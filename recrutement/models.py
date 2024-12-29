from django.db import models

# Create your models here.
from personnel.models import Personnel

class recrutement(models.Model):
 dateRec= models.DateField
 posteRecru = models.CharField
 statutrecrutement = models.CharField