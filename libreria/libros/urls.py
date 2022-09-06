from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'), 
        path('libros/api/', views.LibroListApiView.as_view()),
    path('libros/api/<int:libro_id>/', views.LibroDetailApiView.as_view()),
]