# Importamos utilidades para renderizar plantillas y para devolver un 404 si no existe el objeto
from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente


# Vista de inicio (solo muestra una plantilla básica sin datos)
def home(request):
    # render() recibe: request, ruta de la plantilla, contexto (diccionario)
    return render(request, "tienda/home.html", {})


# Vista que lista todos los productos
def lista_productos(request):
    # ORM: trae todos los productos y los ordena por nombre
    productos = Producto.objects.all().order_by("nombre")
    # Pasamos la lista de productos al template
    return render(request, "tienda/lista_productos.html", {"productos": productos})


# Vista de detalle de un producto
def detalle_producto(request, pk):
    # Busca un producto por clave primaria (pk); si no existe, devuelve 404 automáticamente
    producto = get_object_or_404(Producto, pk=pk)
    # Pasamos el objeto producto a la plantilla
    return render(request, "tienda/detalle_producto.html", {"producto": producto})


# Vista que lista todos los pedidos
def lista_pedidos(request):
    # select_related: trae de una vez la info del cliente (FK) en cada pedido → más eficiente
    # prefetch_related: trae de una vez los productos (M2M) asociados a cada pedido
    # order_by: ordena los pedidos por fecha descendente (los más recientes primero)
    qs = (
        Pedido.objects.select_related("cliente")
        .prefetch_related("productos")
        .order_by("-fecha")
    )
    # Renderizamos la plantilla con el QuerySet
    return render(request, "tienda/lista_pedidos.html", {"pedidos": qs})


# Vista de detalle de un pedido
def detalle_pedido(request, pk):
    # Aquí usamos get_object_or_404 pero sobre un queryset optimizado con select_related y prefetch_related
    pedido = get_object_or_404(
        Pedido.objects.select_related("cliente").prefetch_related("productos"), pk=pk
    )
    # Pasamos el pedido a la plantilla
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})


# Vista de detalle de un cliente
def detalle_cliente(request, pk):
    # Traemos el cliente o 404 si no existe
    cliente = get_object_or_404(Cliente, pk=pk)
    # Desde el cliente accedemos a sus pedidos → relación inversa: cliente.pedidos
    # Optimización: select_related para el cliente y prefetch_related para los productos
    pedidos = (
        cliente.pedidos.select_related("cliente")
        .prefetch_related("productos")
        .order_by("-fecha")
    )
    # Enviamos al template tanto el cliente como su lista de pedidos
    return render(
        request, "tienda/detalle_cliente.html", {"cliente": cliente, "pedidos": pedidos}
    )


from django.views.generic import ListView, DetailView


class ProductoListView(ListView):
    model = Producto
    template_name = "tienda/lista_productos.html"
    context_object_name = "productos"
    ordering = ["nombre"]


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "tienda/detalle_producto.html"
    context_object_name = "producto"


def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = (
        cliente.pedidos.select_related("cliente")
        .prefetch_related("productos")
        .order_by("-fecha")
    )
    return render(
        request, "tienda/detalle_cliente.html", {"cliente": cliente, "pedidos": pedidos}
    )
