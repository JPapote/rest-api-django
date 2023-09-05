# rest-api-django

# Microservicio RESTful con Django

Este proyecto es un microservicio RESTful implementado en Django que permite realizar operaciones básicas de creación y recuperación de datos. El servicio cumple con los siguientes requisitos:

- **Creación de Elementos**: El servicio permite la creación de elementos a partir de una solicitud POST en un endpoint específico. El campo de destino para la conversión de texto a mayúsculas puede ser uno de los siguientes: `field_1`, `author`, o `description`. Si el campo de destino no es válido, se devuelve un error. Los elementos creados se almacenan en una base de datos SQLite.

- **Recuperación de Elementos**: El servicio proporciona un endpoint para recuperar elementos por su ID.

- **Recuperación de Todos los Elementos**: También se ha agregado un endpoint para obtener la lista completa de elementos almacenados en la base de datos.

- **Eliminacion de los elementos**: Se ha agregado un endpoint para eliminar un elemento de la base de datos por su ID

- **Documentacion mas detallada sobre los endpoints**: Se ha agregado un endpoint donde se detalla de una manera mas visual todos los endpoints disponibles y su requerimientos. Dicho endpoint seria: localhost:8000/docs

## Configuración del Proyecto

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona este repositorio en tu máquina:

   ```bash
   git clone <URL_DEL_REPOSITORIO>

pip install -r requirements.txt -
python manage.py makemigrations -
python manage.py migrate -
python manage.py runserver
