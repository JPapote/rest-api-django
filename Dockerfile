<<<<<<< HEAD
# Utiliza una imagen base de Python
FROM python:3.11.5-slim
=======

FROM python:3.11
>>>>>>> c7098b5cd4430e38a173f78ca26e6ac4cc601745


ENV PYTHONUNBUFFERED True
ENV DJANGO_SETTINGS_MODULE res_api_django.settings


WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) e instala las dependencias
COPY ./requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt
# Copia todo el contenido de la aplicación actual en el directorio de trabajo
COPY . ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
