from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Materiel,affect
from .forms import MaterielForm,AffectForm
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    affectations = affect.objects.all()  # Correct capitalization
    materiel = Materiel.objects.all()
    current_date = datetime.now().date()
    
    # Calculate the cutoff date for 5 years
    cutoff_date = current_date - timedelta(days=5*365)
    print("Current Date:", current_date)
    print("Cutoff Date:", cutoff_date)
    older_than_5_years = Materiel.objects.filter(DateAchat__lt=cutoff_date)
    less_than_5_years = Materiel.objects.filter(DateAchat__gte=cutoff_date)

    print("Number of materials older than 5 years:", older_than_5_years.count())
    print("Number of materials less than 5 years:", less_than_5_years.count())

    for materiel in older_than_5_years:
        print(f"Older than 5 years: {materiel.DateAchat}")
    for materiel in less_than_5_years:
        print(f"Less than 5 years: {materiel.DateAchat}")

    if request.method == 'POST':
        form = AffectForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            # Do any additional processing here if needed
            return redirect('dashboard-index')
    else:
        form = AffectForm()
    
    context = {
        'affectations': affectations,
        'form': form,
        'materiel': materiel,
        'older_than_5_years': older_than_5_years,
        'less_than_5_years': less_than_5_years,
    }
    return render(request, 'dashboard/index.html', context)
     
@login_required(login_url='user-login')
def affectation(request):
    # Récupérer la valeur du champ de recherche
    username_query = request.GET.get('username', '')

    # Filtrer les affectations par username si une recherche est effectuée
    if username_query:
        affectations = affect.objects.filter(staff__username__icontains=username_query)
    else:
        affectations = affect.objects.all()

    # Filtrer les matériels non affectés
    materiels_disponibles = Materiel.objects.filter(Etat=False)

    context = {
        'affectations': affectations,
        'materiels_disponibles': materiels_disponibles,  # Liste des matériels disponibles
    }

    return render(request, 'dashboard/affectation.html', context)


@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html', context)


@login_required(login_url='user-login')
def materiel(request):
    # Filtrage des matériels par type
    type_filter = request.GET.get('type')
    if type_filter:
        items = Materiel.objects.filter(Type=type_filter)
    else:
        items = Materiel.objects.all()

    # Gestion du formulaire d'ajout de matériel
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-materiel')
    else:
        form = MaterielForm()

    # Types disponibles pour le filtrage
    types_disponibles = ['Laptop', 'Desktop', 'Ecran', 'Imprimante laser', 'Imprimante thermique', 'PDA']

    context = {
        'items': items,
        'form': form,
        'types_disponibles': types_disponibles,
    }

    return render(request, 'dashboard/materiel.html', context)

@login_required(login_url='user-login')
def materiel_delete(request ,pk):
    item = Materiel.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-materiel')
    return render(request, 'dashboard/materiel_delete.html')


@login_required(login_url='user-login')
def materiel_update(request, pk):
    item = Materiel.objects.get(id=pk)
    if request.method=='POST':
        form = MaterielForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-materiel')
    else:
        form = MaterielForm(instance=item) 
    context={
        'form': form,

    }
    return render(request, 'dashboard/materiel_update.html', context)

from django.contrib.auth.models import User

def affectation(request):
    username_query = request.GET.get('username', '')

    if username_query:
        affectations = affect.objects.filter(staff__username__icontains=username_query)
    else:
        affectations = affect.objects.all()

    materiels_disponibles = Materiel.objects.filter(Etat=False)
    users = User.objects.all()

    context = {
        'affectations': affectations,
        'materiels_disponibles': materiels_disponibles,
        'users': users,
    }

    return render(request, 'dashboard/affectation.html', context)



from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Materiel, affect

def affecter_materiel(request):
    if request.method == 'POST':
        materiel_id = request.POST.get('materiel_id')
        user_id = request.POST.get('user_id')

        materiel = Materiel.objects.get(id=materiel_id)
        user = User.objects.get(id=user_id)

        # Créer une nouvelle affectation
        nouvelle_affectation = affect(Materiel=materiel, staff=user)
        nouvelle_affectation.save()

        # Rediriger vers la page des affectations après l'affectation
        return redirect('affectation')

    # En cas de méthode GET, rediriger vers la page des affectations
    return redirect('affectation')
