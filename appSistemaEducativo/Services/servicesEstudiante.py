import json
from django.http import JsonResponse
import requests

class servicesEstudiante():

    def obtenerEstudiante(user):
        uri = "http://node7299-env-3567666.sp.skdrive.net/rs/alumno/get?usuario="
        url = uri + user
        r = requests.get(url)
        return r.json()
        
