from django.contrib import admin
from django.urls import path
from django.urls import include
from appSistemaEducativo.View import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Controlador.index),
    path('login/',views.Controlador.login),
    path('index/',views.Controlador.indexLg),
    path('onlogin/',views.Controlador.onLogin),
    path('index/profile/',views.Controlador.profile),
    path('buscarDocente/',views.Controlador.buscarDocente),
    path('ofertaAcademica/',views.Controlador.ofertaAcademica),
    path('search/',views.Controlador.search),
    path('profileDocente/',views.Controlador.profileDocente),
    path('matriculacion/',views.Controlador.getMatriculacion),
    path('matriculacion/agregar/',views.Controlador.matriculacionAgregar),
    path('logout/',views.Controlador.logout),
    path('',include('pwa.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
