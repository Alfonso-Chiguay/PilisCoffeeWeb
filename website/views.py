from django.shortcuts import render
from django.views import View
from pos.models import Marca, Categoria

class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')

class Chocolates(View):
    def get(self, request):
        marcas = Marca.objects.filter(id_categoria=2)        
        for marca in marcas:
            nombre_marca = str(marca.nombre)
            if 'NH' in nombre_marca:                
                marca.nombre = nombre_marca.replace("NH","Ñ")            
            
        context = {'marcas': marcas}
        return render(request, 'chocolates.html', context)

class Cafes(View):
    def get(self, request):
        marcas = Marca.objects.filter(id_categoria=1)        
        for marca in marcas:
            nombre_marca = str(marca.nombre)
            if 'NH' in nombre_marca:                
                marca.nombre = nombre_marca.replace("NH","Ñ")
            
            
        context = {'marcas': marcas}
        return render(request, 'cafes.html', context)        


class PostresHelados(View):
    def get(self, request):
        return render(request, 'postres-helados.html')        