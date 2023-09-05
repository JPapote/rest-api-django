# Utiliza una imagen base de Python
FROM python:3.11.5-slim

# Establece variables de entorno para evitar problemas de salida interactiva
ENV PYTHONUNBUFFERED True
ENV DJANGO_SETTINGS_MODULE res_api_django.settings

# Crea y establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) e instala las dependencias
COPY ./requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt
# Copia todo el contenido de la aplicación actual en el directorio de trabajo
COPY . ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
