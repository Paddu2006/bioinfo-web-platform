from django.urls import path
from . import views

urlpatterns = [
    path('',          views.home,              name='home'),
    path('dna/',      views.dna_analyzer,      name='dna_analyzer'),
    path('mutation/', views.mutation_detector,  name='mutation_detector'),
    path('fasta/',    views.fasta_analyzer,     name='fasta_analyzer'),
    path('history/',  views.history,            name='history'),
]