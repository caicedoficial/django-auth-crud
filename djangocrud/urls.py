"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registrar/', views.registrar, name='registrar'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas_completadas/', views.tareas_completadas, name='tareas_completadas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:task_id>/', views.tareas_detalles, name='tareas_detalles'),
    path('tareas/<int:task_id>/completar/', views.completar_tareas, name='completar_tareas'),
    path('tareas/<int:task_id>/eliminar/', views.eliminar_tareas, name='eliminar_tareas'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion')
]
