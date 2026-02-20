from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.home, name="home"),
    # Ruta raíz ("/") → ejecuta la vista 'home'.
    # 'name="home"' permite referenciarla en plantillas con {% url 'tienda:home' %}.
    path("productos/", views.lista_productos, name="lista_productos"),
    # Ruta "/productos/" → muestra la lista de productos.
    # Usa la vista 'lista_productos'.
    path("productos/<int:pk>/", views.detalle_producto, name="detalle_producto"),
    # Ruta dinámica "/productos/1/" o "/productos/5/"...
    # <int:pk> captura el número de ID (primary key) del producto.
    # Llama a la vista 'detalle_producto' con ese 'pk'.
    path("pedidos/", views.lista_pedidos, name="lista_pedidos"),
    # Ruta "/pedidos/" → muestra todos los pedidos registrados.
    # Usa la vista 'lista_pedidos'.
    path("pedidos/<int:pk>/", views.detalle_pedido, name="detalle_pedido"),
    # Ruta dinámica "/pedidos/3/"...
    # Llama a 'detalle_pedido' mostrando info de un pedido específico.
    path("clientes/<int:pk>/", views.detalle_cliente, name="detalle_cliente"),
    # Ruta dinámica "/clientes/2/"...
    # Muestra los datos de un cliente específico y sus pedidos.
]
