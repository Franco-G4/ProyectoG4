from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def inicio(request):

    return render(request, "proyectofinalapp/inicio.html")


def servicios(request):

    return render(request, "proyectofinalapp/servicios.html")


def tienda(request):

    return render(request, "proyectofinalapp/tienda.html")


def nosotros(request):

    return render(request, "proyectofinalapp/nosotros.html")

#formulario de contacto
def contacto(request):
    
    if request.method=="POST":

        subject=request.POST["Nombre"]
        #asunto=request.POST["Asunto"]
        message=request.POST["Mensaje"] + " " + request.POST["Email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["pruebasvariasprogramacion@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, "proyectofinalapp/carrusel.html")

    return render(request, "proyectofinalapp/contacto.html")


