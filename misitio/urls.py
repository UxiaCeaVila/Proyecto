from django.urls import path
from . import views

app_name="gestion"
urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('robots/verproducts', views.listaproducts, name="listarProducts"),
    path('robots/crearproducts', views.ventaproducts, name="nuevoProducts"),
    path('robots/borrar/<numserie>', views.borrarProducto, name="borrarProducts"),
    path('clientes/listarClientes', views.listaclients, name="listarClientes"),
    path('robots/nuevoCliente', views.nuevoclient, name="nuevoCliente"),
    path('cliente/borrar/<idclient>', views.borrarCliente, name="borrarCliente"),
    path('ventas/listarventas', views.listaventas, name="listarVentas"),
    path('ventas/nuevaventa', views.nuevaventa, name="nuevaVenta"),
    path('ventas/devolver/<idventa>', views.borrarventa, name="devolverVenta"),
    path('provedores/listaprovedores', views.listaprovedores, name="listaProvedores"),
    path('provedores/nuevoprovedor', views.nuevoprovedor, name="nuevoProvedor"),
    path('provedores/borrar/<idprovedor>', views.borrarprovedor, name="borrarProvedor"),
    path('provedores/productos/listaproductprovedores', views.listaproductprovedores, name="listaProductProvedores"),
    path('provedores/productos/nuevoproductprovedor', views.nuevoproductprovedor, name="nuevoProductProvedor"),
    path('provedores/productos/borrar/<idproductoprove>', views.borrarproductprovedor, name="borrarProductoProvedor"),
]