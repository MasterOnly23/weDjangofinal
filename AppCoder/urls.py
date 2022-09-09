from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores)
]