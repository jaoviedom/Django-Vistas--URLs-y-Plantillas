# Guía de Despliegue en PythonAnywhere

Este documento detalla los pasos necesarios para poner en producción este proyecto de Django en [PythonAnywhere](https://www.pythonanywhere.com/).

## 1. Clonar el repositorio

Accede a la consola Bash de PythonAnywhere y clona tu repositorio (reemplaza `<URL_DEL_REPO>` por la URL real):

```bash
git clone <URL_DEL_REPO>
cd "02 Vistas, URLs y Plantillas"
```

## 2. Crear y configurar el entorno virtual

Crea un entorno virtual para aislar las dependencias del proyecto:

```bash
mkvirtualenv --python=/usr/bin/python3.10 venv-proyecto
pip install -r requirements.txt
```

*Nota: Asegúrate de que la versión de Python coincida con la que prefieras usar en la pestaña 'Web'.*

## 3. Configurar la aplicación Web

En el panel de control de PythonAnywhere, ve a la pestaña **Web**:

1. Haz clic en **Add a new web app**.
2. Selecciona **Manual configuration** (No selecciones Django directamente, ya que usaremos el código que ya tenemos).
3. Selecciona la versión de Python (ej. Python 3.10).

### Configuración del Entorno Virtual (Virtualenv)
En la sección **Virtualenv**, introduce la ruta completa a tu entorno virtual:
`/home/jaoviedom/.virtualenvs/venv-proyecto`

### Configuración del Código
- **Source code:** `/home/jaoviedom/02 Vistas, URLs y Plantillas`
- **Working directory:** `/home/jaoviedom/02 Vistas, URLs y Plantillas`

## 4. Configurar el archivo WSGI

Haz clic en el enlace del archivo de configuración WSGI (normalmente `/var/www/jaoviedom_pythonanywhere_com_wsgi.py`) y edítalo para que tenga el siguiente contenido (asegúrate de borrar el contenido por defecto):

```python
import os
import sys

# Añade la ruta del proyecto al sys.path
path = '/home/jaoviedom/02 Vistas, URLs y Plantillas'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Configuración específica para PythonAnywhere
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 5. Base de Datos y Archivos Estáticos

Regresa a la consola Bash y ejecuta los siguientes comandos dentro de tu proyecto:

```bash
# Aplicar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic
```

## 6. Configuración de Archivos Estáticos en la pestaña Web

En la pestaña **Web**, busca la sección **Static files** y añade:

- **URL:** `/static/`
- **Directory:** `/home/jaoviedom/02 Vistas, URLs y Plantillas/staticfiles`

## 7. Variables de Entorno (Opcional)

Si utilizas un archivo `.env` (como sugiere la presencia de `python-dotenv` en requirements.txt), puedes crear un archivo `.env` en el directorio raíz del proyecto en PythonAnywhere:

```bash
nano .env
```
Añade tus variables:
```env
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=tu_clave_secreta_aqui
```

## 8. Recargar la aplicación

Finalmente, vuelve a la pestaña **Web** y haz clic en el botón verde **Reload jaoviedom.pythonanywhere.com**.

¡Tu aplicación debería estar en línea!
