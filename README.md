# Ejercicios 1 y 2

### Ejercicio 1: Docker

Configura un ambiente en docker que permita ejecutar un entorno web con el stack a tu elección. 
El contenedor de la base de datos debe ser diferente al que contenga tu aplicación, ej: Contenedor 1: Nginx, Contenedor 2: Mysql (composición de servicios docker)

### Ejercicio 2: API REST + CRUD

Dentro del ambiente dockerizado desarrolla una API Rest, con el stack de tu preferencia, que implemente un CRUD de una entidad tipo 'empresa'. Preocupate de incluir un script que genere N registros con datos "fake" (utilizando una librería faker).



###  Software requerido
```text
   DOCKER  https://www.docker.com/products/docker-desktop
   VISUAL CODE https://code.visualstudio.com/
```


###  Pasos para crear los contenedores Docker

```text
docker-compose up -d --build
docker exec -it django python manage.py makemigrations
docker exec -it django python manage.py migrate
docker exec -it django python manage.py createsuperuser
docker-compose up
```

###  Abrir navegador 

```text
http://localhost:8000/
```

