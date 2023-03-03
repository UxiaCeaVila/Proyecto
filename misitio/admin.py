from django.contrib import admin
from .models import Product
from .models import Client, Venta, Proveedor ,ProductosProvedor
# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Venta)
admin.site.register(Proveedor)
admin.site.register(ProductosProvedor)