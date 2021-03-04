from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



# INICIO ---------------------------------------------------
def inicio(request):

    return render(request, "proyectofinalapp/inicio.html")



# SERVICIOS ------------------------------------------------
from .models import Persona

def servicios(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        persona = Persona.objects.all()
        return render(request, "proyectofinalapp/servicios.html", {'personas': persona})
    # En otro caso redireccionamos al login
    return redirect('/login')



# CONTACTO --------------------------------------------------
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


from django.shortcuts import render, redirect



# REGISTER -----------------------------------------------

from django.contrib.auth.forms import UserCreationForm

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/servicios/')
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "proyectofinalapp/register.html", {'form': form})



# LOGIN -------------------------------------------------

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/servicios')

    # Si llegamos al final renderizamos el formulario
    return render(request, "proyectofinalapp/login.html", {'form': form})



# LOGOUT -------------------------------------------------------

from django.contrib.auth import logout as do_logout

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/servicios')



# ADD -----------------------------------------------------------
from .forms import PersonaForm

def add(request):
    # Creamos un formulario vacío
    form = PersonaForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = PersonaForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/servicios')

    # Si llegamos al final renderizamos el formulario
    return render(request, "proyectofinalapp/add.html", {'form': form})



# EDIT -----------------------------------------------------------
from .models import Persona

def edit(request, persona_id):
    # Recuperamos la instancia de la persona
    instancia = Persona.objects.get(id=persona_id)

    # Creamos el formulario con los datos de la instancia
    form = PersonaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = PersonaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "proyectofinalapp/edit.html", {'form': form})



# LISTA -----------------------------------------------------------

def lista(request):
    #instancia = Persona.objects.get(id=persona_id)
    #persona = PersonaForm(instance=instancia)
    #return render(request, "users/lista.html", {'personas': persona})
    persona = Persona.objects.all()
    return render(request, "proyectofinalapp/lista.html", {'personas': persona})
        



# DELETE -----------------------------------------------------------

def delete(request, persona_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Persona.objects.get(id=persona_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('/servicios')