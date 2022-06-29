from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Mascotas', views.mascotas, name="Mascotas"),
    path('Dueños', views.dueños, name="Dueños"),
    path('Encargados', views.encargados, name="Encargados"),
    path('buscar/', views.buscar),
]