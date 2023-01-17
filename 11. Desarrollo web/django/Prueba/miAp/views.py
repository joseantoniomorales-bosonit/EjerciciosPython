from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("Hola mundo")

def parametros(request,id):
    return HttpResponse("El id es: {0}".format(id))