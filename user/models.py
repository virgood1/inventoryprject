from django.db import models
from django.contrib.auth.models import User

# Create your models here.
AGENCE = (
    ('CASABLANCA','CASABLANCA'),
    ('TANGER','TANGER'),
)

class profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    NumImmatriculatione=models.CharField(max_length=100, null=True)
    Nom=models.CharField(max_length=100, null=True)
    Prenom=models.CharField(max_length=100, null=True)
    Agence=models.CharField(max_length=100,choices=AGENCE, null=True)
    Service=models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.staff.username}--Profile'