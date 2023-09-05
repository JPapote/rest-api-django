
FROM python:3.11


ENV PYTHONUNBUFFERED True
ENV DJANGO_SETTINGS_MODULE res_api_django.settings


WORKDIR /app

EXPOSE 8000


COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install pip-tools

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "8000"]
