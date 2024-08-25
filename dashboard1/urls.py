from django.urls import path 
from . import views

urlpatterns =[
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('affectation/',views.affectation, name='dashboard-affectation'),
    path('materiel/',views.materiel, name='dashboard-materiel'),
    path('materiel/delete/<int:pk>',views.materiel_delete, name='dashboard-materiel-delete'),
    path('affecter-materiel/', views.affecter_materiel, name='affecter_materiel'),
    path('materiel/update/<int:pk>',views.materiel_update, name='dashboard-materiel-update'),
    path('affectation/', views.affectation, name='affectation'),

]