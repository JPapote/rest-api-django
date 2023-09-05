# Utiliza una imagen base de Python
FROM python:3.11

# Establece variables de entorno para evitar problemas de salida interactiva
ENV PYTHONUNBUFFERED True
ENV DJANGO_SETTINGS_MODULE res_api_django.settings

# Crea y establece el directorio de trabajo en /app
WORKDIR /app

EXPOSE 8000

# Copia los archivos de requerimientos (requirements.txt) e instala las dependencias
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install pip-tools

RUN pip install --no-cache-dir -r requirements.txt
# Copia todo el contenido de la aplicación actual en el directorio de trabajo
COPY . /app/

CMD ["python", "manage.py", "runserver", "8000"]
