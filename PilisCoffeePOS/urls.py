from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('pos/', include('pos.urls'), name='pos'),
    path('', include('website.urls'), name='website_main'),
]
