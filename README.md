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

###  Configuración contenedores
```text
   version: "3.8"

services:                   
    #Nginx Service
    webserver:
        image: nginx:alpine
        container_name: nginx
        restart: unless-stopped
        tty: true
        ports:
            - "80:80"
            - "443:443"
            - "81:81"   
        volumes:
            - ./src:/src
            - ./config/nginx:/etc/nginx/conf.d
            - /static:/static  
        depends_on:
            - django  

    #Django Service
    django:
        build: .
        container_name: django
        command: python manage.py runserver 0.0.0.0:8000
        #command: bash -c "python manage.py makemigrations && migrate mydjango.wsgi -b 0.0.0.0:8000"    
        volumes: 
            - .:/usr/src/app
            - /static:/static
        ports:
            - "8000:8000"
        depends_on:
            #- db            
            - pgdb             
    #MySQL Service
    db:
        image: mysql:5.7.32
        container_name: mysql
        restart: unless-stopped
        tty: true
        ports:
        - "3306:3306"
        environment:       
            MYSQL_DATABASE: enviame     
            MYSQL_ROOT_PASSWORD: 123
            SERVICE_TAGS: dev
            SERVICE_NAME: mysql         
    #POSTGRES Service
    pgdb:
        image: postgres:10.5
        container_name: postgresql
        restart: unless-stopped
        tty: true
        ports:
        - "5432:5432"
        environment: 
            - POSTGRES_DB=enviame
            - POSTGRES_USER=postgres
            - POSTGRES_PASSWORD=123
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

