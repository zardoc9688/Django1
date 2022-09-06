
#imports
from django.template import loader
from django.http import HttpResponse

#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Modelos
from .models import Libro
from .serializers import LibroSerializer

def index(request):
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))

class LibroListApiView(APIView):

    def get(self,request,*args, **kwargs):
        '''
        Lista todos los libros en base de datos
        '''
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, *args, **kwargs):
        '''
        Crea un libro en base de datos
        '''
        data = {
            'autor': request.data.get('autor'),
            'categoria': request.data.get('categoria'),
            'titulo': request.data.get('titulo'),
            'descripcion': request.data.get('descripcion'),
            'fecha_pub': request.data.get('fecha_pub')
        }

        serializer = LibroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibroDetailApiView(APIView):

    def get_object(self,libro_id):
        '''
        Metodo de ayuda para retornar un libro con un id Dado
        '''
        try:
            return Libro.objects.get(id=libro_id)
        except Libro.DoesNotExist:
            return None
        
    def get(self,request,libro_id, *args, **kwargs):
        '''
        Permite obtener un libro por ID
        '''
        libro_instance = self.get_object(libro_id)
        if not libro_instance:
            return Response(
                {"res":"El libro con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        serializer = LibroSerializer(libro_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, libro_id, *args, **kwargs):
        '''
        Actualiza un libro por su ID
        '''
        libro_instance = self.get_object(libro_id)
        if not libro_instance:
            return Response(
                {"res":"El libro con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'autor': request.data.get('autor'),
            'categoria': request.data.get('categoria'),
            'titulo': request.data.get('titulo'),
            'descripcion': request.data.get('descripcion'),
            'fecha_pub': request.data.get('fecha_pub')
        }

        serializer = LibroSerializer(instance = libro_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,libro_id, *args, **kwargs):
        '''
        Elimina el libro con el ID dado
        '''
        libro_instance = self.get_object(libro_id)
        if not libro_instance:
            return Response(
                {"res":"El libro con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        libro_instance.delete()
        return Response(
            {"res":"Object Deleted"},
            status=status.HTTP_200_OK
        )
