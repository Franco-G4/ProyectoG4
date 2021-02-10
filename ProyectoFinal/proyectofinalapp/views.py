from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):

    return render(request, "proyectofinalapp/inicio.html")


def servicios(request):

    return HttpResponse("servicios")


def tienda(request):

    return HttpResponse("tienda")


def nosotros(request):

    return HttpResponse("nosotros")

