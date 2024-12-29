from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Favori(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoris")
    nom = models.CharField(max_length=100)  # Nom de la fonctionnalité
    url = models.CharField(max_length=255)  # URL de la fonctionnalité
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.nom}"