from django.shortcuts import render
from django.views import View

class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')

class Chocolates(View):
    def get(self, request):
        return render(request, 'chocolates.html')

class Cafes(View):
    def get(self, request):
        return render(request, 'cafes.html')        


class PostresHelados(View):
    def get(self, request):
        return render(request, 'postres-helados.html')        