from django.contrib import admin
from .models import Post #se importa la clase de  los modelos que se quieren agregar al panel de administrador

admin.site.register(Post) #se registra el modelo (revisar notas)
