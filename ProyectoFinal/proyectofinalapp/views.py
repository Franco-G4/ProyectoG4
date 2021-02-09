from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):

    return HttpResponse("Inicio")


def servicios(request):

    return HttpResponse("servicios")


def tienda(request):

    return HttpResponse("tienda")


def nosotros(request):

    return HttpResponse("nosotros")
