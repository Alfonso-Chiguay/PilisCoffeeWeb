from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect  ('home_pos')
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('home_pos')
                else:
                    messages.error(request, 'Los datos no son correctos')
                    return redirect('login')
            else:
                messages.error(request, 'Datos incorrectos')
                return redirect('login')

        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

class Logout(View):
    def get(self, request):
        user = request.user
        if user is not None:
            logout(request)
            
        return redirect('login')

class Home(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'pos_home.html')

class VentasHome(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'ventas_home.html')

class ReportesHome(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'reportes.html')        

class InventarioHome(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'inventario.html')    

class CrearVenta(LoginRequiredMixin,View):

    def get(self, request):
        context = {'productos': Producto.objects.all()}
        return render(request, 'ventas/nueva_venta.html', context)