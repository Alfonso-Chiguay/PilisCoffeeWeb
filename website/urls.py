from django.urls import path
from .views import HomePage, Cafes, Chocolates, PostresHelados

urlpatterns = [
    path('', HomePage.as_view(), name='homeweb'),
    path('cafes/',  Cafes.as_view(), name='cafes'),
    path('chocolates/', Chocolates.as_view(), name='chocolates'),
    path('postres-helados/', PostresHelados.as_view(), name='postres-helados')
]
