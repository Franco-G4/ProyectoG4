from django.urls import path

from proyectofinalapp import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('servicios/', views.servicios, name="servicios"),
    path('tienda/', views.tienda, name="tienda"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
]
