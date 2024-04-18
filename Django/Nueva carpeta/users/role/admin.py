from django.contrib import admin
from .models import Producto, PermisoProducto


admin.site.register(Producto)
admin.site.register(PermisoProducto)