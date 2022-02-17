from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
import requests
from django.contrib import messages
from appSistemaEducativo.Services.servicesEstudiante import servicesEstudiante

status = False
datosUser = {}
asignaturas = {}

class Controlador():

    def login(request):
        global status
        if(status==False):
            return render(request,"login.html")
        else:
            return redirect("/index/")

    def index(request):
        global status
        if(status==False):
            return render(request,"index.html")
        else:
            return redirect("/index/")
        
    
    def indexLg(request):
        global status
        print(status)
        return render(request,"indexLg.html")

    @api_view(['GET','POST'])
    def onLogin(request):
        global status
        global datosUser
        if(status==False):
            user = request.POST.get('login')
            password = request.POST.get('password')
            if(user!=""):
                print(user)
                print(password)
                data = {'user': user , 'pass':password}
                datosUser = data
                r = requests.post("http://node7299-env-3567666.sp.skdrive.net/rs/login",json=data)
                resultado = r.json()
                response = resultado.get('response')
                if(response=="OK."):
                    status = True
                    return redirect("/index/")
                else:
                    messages.error(request, response)
                    return redirect("/login/")
            else:
                messages.error(request, "Error: ingrese datos por favor.")
                return redirect("/login/")
        else:
            return redirect("/index/")

    def profile(request):
        global datosUser
        datos = servicesEstudiante.obtenerEstudiante(datosUser.get("user"))
        print(datos)
        return render(request,"profile.html",{"nombre":datos.get("nombre"),"direccion":datos.get("direccion"),"fechaN":datos.get("fechaNacimiento"),
            "correo":datos.get("correo"),"contraseña":datos.get("contraseña")})


    def buscarDocente(request):
        return render(request,"BuscarDocente.html")

    def ofertaAcademica(request):
        r = requests.get("http://node7299-env-3567666.sp.skdrive.net/rs/alumno/asignaturas")
        respuesta = r.json()
        datos = {
            'datos':respuesta 
        }
        print(datos)
        return render(request,"OfertaAcademica.html",datos)

    @api_view(['GET','POST'])
    def search(request):
        global datosUser
        cedula = request.POST.get('cedula')
        r = requests.get("http://node7299-env-3567666.sp.skdrive.net/rs/docente?cedula="+cedula)
        datos = r.json()
        datosUser = datos
        return redirect("/profileDocente/")

    def profileDocente (request):
        global datosUser
        print(datosUser)
        return render(request,"profileDocente.html",{"nombre":datosUser.get("nombre"),"direccion":datosUser.get("direccion"),"fechaN":datosUser.get("fechaNacimiento"),
            "correo":datosUser.get("correo"),"contrasena":datosUser.get("contrasena")})
    
    def getMatriculacion(request):
        global datosUser, status, asignaturas
        if(status):
            datos = servicesEstudiante.obtenerEstudiante(datosUser.get("user"))
            asignaturas = datos.get("asignaturas")
            print(asignaturas)
            return render(request,"matriculacion.html",{"nombre":datos.get("nombre"),"asignaturas":asignaturas,"status":status})
        else:
            return redirect("/login/") 
    
    def matriculacionAgregar(request):
        global datosUser
        datos = servicesEstudiante.obtenerEstudiante(datosUser.get("user"))
        codigo =  request.POST.get('codAsignatura')
        print(codigo)
        print(datos.get("cedula"))
        requests.post("http://node7299-env-3567666.sp.skdrive.net/rs/alumno/matriculacion?cedula="+datos.get("cedula")+"&asignatura="+codigo)
        return redirect("/matriculacion/") 

    def logout(request):
        global status, datosUser, asignaturas
        status = False
        datosUser = {}
        asignaturas = {}
        return redirect("/")

        
        
