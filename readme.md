# Proyecto Docker con Django
 - Fuentes:
    * (https://github.com/harveydf/tutoriales-django-environments)
    * https://www.youtube.com/watch?v=_DJahG4FiOE  
 - Crear el volumen aparte con el comando:
    ```sh
    docker volume create --name=bd_data
    ```
 - Ubicarnos dentro de la carpeta **webapp**
 - Comando para correr el django en el contenedor:
    ```sh    
    $ docker-compose run web django-admin.py startproject proy_environments .
    ```
 - mi carpeta queda asi:
   ```sh 
    $ tree
      webapp/
      ├── Dockerfile
      ├── manage.py
      ├── proy_logging
      │   ├── asgi.py
      │   ├── db.sqlite3
      │   ├── __init__.py
      │   ├── settings
      │   │   ├── base.py
      │   │   ├── dev.py
      │   │   └── __init__,py
      │   ├── urls.py
      │   └── wsgi.py
      └── requirements
         ├── base.txt
         └── dev.txt
    ```
 - Agregar las variables de conexion al postgresql y el host permitido:
   ```
    ALLOWED_HOSTS = ['*']
    ...
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydb',
            'USER': 'example',
            'PASSWORD': 'secret',
            'HOST': 'db',
            'PORT': '5432',
        }
    }
    ```
 - Levantar nuevamente el contenedor:
   ```sh
    docker-compose up -d
   ```
 - Visualizar los logs:
   ```sh
    $ docker-compose logs web
    $ docker-compose logs db
   ```
 - Ejecutar comandos docker:
   ```sh
   docker exec -ti 004_django_logs_web_1 python3 manage.py migrate
   docker exec -ti 004_django_logs_web_1 python3 manage.py makemigrations
   docker exec -ti 004_django_logs_web_1 python3 manage.py createsuperuser
   docker exec -ti 004_django_logs_web_1 python3 manage.py shell
   docker exec -ti 004_django_logs_web_1 python3 manage.py startapp <new_app>
   ```

---