from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):

    return render(request, "proyectofinalapp/inicio.html")


def servicios(request):

    return render(request, "proyectofinalapp/servicios.html")


def tienda(request):

    return render(request, "proyectofinalapp/tienda.html")


def nosotros(request):

    return render(request, "proyectofinalapp/nosotros.html")

