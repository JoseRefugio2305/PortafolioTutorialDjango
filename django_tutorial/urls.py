"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from generator import views
from portfolio import views as portfolioviews
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-pass/',views.about, name='about'),
    path('pass-generator',views.home, name='homepass'),#Ruta inicial,
    path('generate-password', views.password, name='password'),
    path('',  portfolioviews.home, name='home'),
    #Con lo siguiente se importan todas las rutas propias de la app blog, usando el include
    path('blog/', include('blog.urls'))
]

#Esto es necesario para agregar las rutas estaticas y no haya problema al revisar archivos estaticos como imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)