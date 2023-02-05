from django.urls import path
from .views import Home, Login, Logout, VentasHome, InventarioHome, ReportesHome, CrearVenta


urlpatterns = [    
    path('', Home.as_view(), name='home_pos'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('ventas/', VentasHome.as_view(), name='ventas'),
    path('inventario/', InventarioHome.as_view(), name='inventario'),
    path('reportes/', ReportesHome.as_view(), name='reportes'),
    path('ventas/nueva_venta/', CrearVenta.as_view(), name='nueva_venta'),
]
