from django import forms
from .models import Materiel,affect

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['NumInventaire','Type','NumSerie','Hostname','Marque','Modele','DateAchat']

class AffectForm(forms.ModelForm):
    class Meta:
        model = affect
        fields = ['Materiel']