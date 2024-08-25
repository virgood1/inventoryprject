from django.db import models
from django.contrib.auth.models import User  

TYPE = (
    ('Laptop','Laptop'),
    ('Desktop','Desktop'),
    ('Ecran','Ecran'),
    ('Imprimante laser','Imprimante laser'),
    ('Imprimante thermique','Imprimante thermique'),
    ('PDA','PDA'),
)

AGENCE = (
    ('CASABLANCA','CASABLANCA'),
    ('TANGER','TANGER'),
)

# Create your models here.
class Materiel(models.Model):
    NumInventaire = models.CharField(max_length=100, null=True)
    Type = models.CharField(max_length=100, choices=TYPE, null=True)
    NumSerie = models.CharField(max_length=100, null=True)
    Hostname = models.CharField(max_length=100, null=True)
    Marque = models.CharField(max_length=100, null=True)
    Modele = models.CharField(max_length=100, null=True)
    DateAchat = models.DateField(null=True)
    Etat = models.BooleanField(default=False)  # Ajout de l'attribut Etat

    def __str__(self):
        return f'{self.Type,self.NumInventaire}'
        



class staff(models.Model):
    NumImmatriculatione=models.CharField(max_length=100, null=True)
    Nom=models.CharField(max_length=100, null=True)
    Prenom=models.CharField(max_length=100, null=True)
    Agence=models.CharField(max_length=100,choices=AGENCE, null=True)
    Service=models.CharField(max_length=100, null=True)
        
    def __str__(self):
        return f'{self.Nom}'

class affect(models.Model):
    Materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        # Avant de sauvegarder l'affectation, on met à jour l'état du matériel
        if self.Materiel:
            self.Materiel.Etat = True
            self.Materiel.save()
        super(affect, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Avant de supprimer l'affectation, on met à jour l'état du matériel
        if self.Materiel:
            self.Materiel.Etat = False
            self.Materiel.save()
        super(affect, self).delete(*args, **kwargs)

    
    def __str__(self):
        return f'{self.Materiel} affected to {self.staff}'