from django.contrib import admin
from .models import project

#con esto le agregamos al panel de administrador la posibilidad de interactuar con el modelo creado en models de portfolio
admin.site.register(project)
