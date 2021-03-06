from django.urls import path

from proyectofinalapp import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('servicios/', views.servicios, name="servicios"),

    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add/', views.add),
    path('edit/<int:persona_id>', views.edit),
    path('lista', views.lista),
    path('delete/<int:persona_id>', views.delete),

    path('contacto/', views.contacto, name="contacto"),

]
