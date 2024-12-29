from django.db import models

# Create your models here.
class service(models.Model):
 nom= models.CharField(max_length=50)
 description= models.CharField(max_length=300)