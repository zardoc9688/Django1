from django.shortcuts import render

#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
#importar modelo y formulario
from .models import Autor
from .forms import AutorForm


#Vista para listar autores
def listarAutores(request):
    autores = Autor.objects.all()
    context = {'autores':autores}
    template = loader.get_template('autores/autores.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def autor_view(request, id):
    context = {}
    context['object'] = Autor.objects.get(id = id)
    return render(request,'autores/autor_detalle.html',context)

#vista para crear autores.
def crear_autor(request):
    context = {}
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('autores')    
    context['form'] = form
    return render(request,'autores/crear_autor.html', context)


#vista para actualizar autores
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_autor(request,id):
    context = {}
    obj = get_object_or_404(Autor, id = id)
    #formulario que contiene la instancia
    form = AutorForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('autores')    
    context['form'] = form
    return render(request, "autores/actualizar_autor.html", context)


#Vista para eliminar un autor
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Autor, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('autores')    
    return render(request, "autores/eliminar_autor.html", context)