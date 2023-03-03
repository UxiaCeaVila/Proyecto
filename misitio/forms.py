from django import forms
from .models import Product
from .models import Client, Venta, ProductosProvedor, Proveedor

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['numserie', 'nombre', 'modelo', 'version', 'precio']
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['idclient', 'nombre', 'dniclient', 'fecnac']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['idventa', 'client', 'product', 'precio', 'unidades']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['idprovedor', 'nombre', 'lolcalizacion']

class ProductosProvedorForm(forms.ModelForm):
    class Meta:
        model = ProductosProvedor
        fields = ['idproductoprove', 'nombre', 'provedor', 'precio', 'unidades']