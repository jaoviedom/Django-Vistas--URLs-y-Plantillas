# Despliegue desde GitHub a PythonAnywhere

Esta guía asume que tu proyecto ya se encuentra en un repositorio de **GitHub** y que deseas usarlo como fuente para tu sitio en PythonAnywhere.

## 1. Preparación Local

Antes de subir tus cambios a GitHub, asegúrate de que el proyecto esté listo:

1. **Actualiza las dependencias:**
   ```bash
   pip freeze > requirements.txt
   ```
2. **Sube tus cambios:**
   ```bash
   git add .
   git commit -m "Preparado para despliegue"
   git push origin main
   ```

## 2. Configuración Inicial en PythonAnywhere (Solo la primera vez)

Si es la primera vez que despliegas:

1. **Abre una consola Bash en PythonAnywhere.**
2. **Clona tu repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPO.git
   cd TU_REPO
   ```
3. **Crea el entorno virtual:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 venv-proyecto
   pip install -r requirements.txt
   ```

## 3. Flujo de Actualización (Cuando hagas cambios)

Cada vez que actualices tu código en GitHub y quieras verlo en producción:

1. **En la consola de PythonAnywhere:**
   ```bash
   cd ~/TU_REPO
   git pull origin main
   workon venv-proyecto
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
2. **Recarga la Web App:**
   Ve a la pestaña **Web** en PythonAnywhere y presiona **Reload**.

## 4. Recordatorios Importantes

- **ALLOWED_HOSTS:** Asegúrate de que `tu_usuario.pythonanywhere.com` esté en la lista en `settings.py`.
- **Variables de Entorno:** Crea un archivo `.env` en la carpeta raíz de tu proyecto en PythonAnywhere para manejar el `SECRET_KEY` y `DEBUG=False`.
- **Ruta WSGI:** Verifica que la ruta en el archivo de configuración WSGI apunte correctamente a la carpeta donde clonaste el repositorio.

---
*Tip: Puedes automatizar el 'Reload' usando el comando `touch /var/www/tu_usuario_pythonanywhere_com_wsgi.py` al final de tus comandos de actualización en la consola.*
