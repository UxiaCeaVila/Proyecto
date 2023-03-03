from datetime import timezone

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .forms import ClientForm, VentaForm, ProductosProvedorForm, ProveedorForm
from .models import Product
from .models import Client,Venta,Proveedor,ProductosProvedor


# Create your views here.

def frontpage(request):
    return render(request,'frontpage.html')
def listaproducts(request):
    products = Product.objects.order_by("numserie")
    return render(request,'listarProducts.html', {'products': products})
def ventaproducts(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            product = form.save()
            product.save()
    else:
        print("no vamos bien")
        form = ProductForm()
    return render(request,'nuevoProducto.html',{'form': form})
def borrarProducto(request, numserie):
   product = get_object_or_404(Product, numserie=numserie)
   product.delete()
   return redirect('gestion:listarProducts')
def listaclients(request):
    clients = Client.objects.order_by("idclient")
    return render(request,'listarClientes.html', {'clients': clients})
def nuevoclient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            client = form.save()
            client.save()
    else:
        print("no vamos bien")
        form = ClientForm()
    return render(request,'nuevoProducto.html',{'form': form})
def borrarCliente(request, idclient):
   client = get_object_or_404(Client, idclient=idclient)
   client.delete()
   return redirect('gestion:listarClientes')
def listaventas(request):
    ventas = Venta.objects.order_by("idventa")
    return render(request,'listarVentas.html', {'ventas': ventas})
def nuevaventa(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            venta = form.save()
            venta.save()
    else:
        print("no vamos bien")
        form = VentaForm()
    return render(request,'nuevaVenta.html',{'form': form})
def borrarventa(request, idventa):
   venta = get_object_or_404(Venta, idventa=idventa)
   venta.delete()
   return redirect('gestion:listarVentas')

def listaprovedores(request):
    provedores = Proveedor.objects.order_by("idprovedor")
    return render(request,'listarProvedores.html', {'provedores': provedores})
def nuevoprovedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            venta = form.save()
            venta.save()
    else:
        print("no vamos bien")
        form = ProveedorForm()
    return render(request,'nuevoProveedor.html',{'form': form})
def borrarprovedor(request, idprovedor):
   provedor = get_object_or_404(Proveedor, idprovedor=idprovedor)
   provedor.delete()
   return redirect('gestion:listaProvedores')

def listaproductprovedores(request):
    productosprov = ProductosProvedor.objects.order_by("idproductoprove")
    return render(request,'listarProductosProveedor.html', {'productosprov': productosprov})
def nuevoproductprovedor(request):
    if request.method == 'POST':
        form = ProductosProvedorForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            venta = form.save()
            venta.save()
    else:
        print("no vamos bien")
        form = ProductosProvedorForm()
    return render(request,'nuevoProductoProvedor.html',{'form': form})
def borrarproductprovedor(request, idproductoprove):
   productosprov = get_object_or_404(ProductosProvedor, idproductoprove=idproductoprove)
   productosprov.delete()
   return redirect('gestion:listaProductProvedores')