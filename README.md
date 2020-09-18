# Sistema Gestion de Pedidos -- En Progreso
Projecto Reto - [3/A]

![Alt text](https://i.imgur.com/zTVAx2u.png)
![Alt text](https://i.imgur.com/rrcRYwr.png)
![Alt text](https://i.imgur.com/yzyeorJ.png)
![Alt text](https://i.imgur.com/v4QMixK.png)
![Alt text](https://i.imgur.com/Yl54EqO.png)

# Entorno Virutal

Deberas tener la version de python 3.6.9 hasta la 3.7 solo en esas versiones e estable el projecto

Use la libreria  [virtualenv](https://pypi.org/project/virtualenv/) para crear el entorno
## Instalacion
```bash
>> pip install virtualenv or pip3 install virtualenv
```
## Creacion del entorno Virtual

recomendacion crear el entorno virtual fuera del projecto

```bash
>> python3 -m venv nombredelentorno or python -m venv nombredelentorno
```


## Activacion del entorno virtual

rediriguirse al entorno virutal donde fue creado

**WINDOWS**
```bash
c:\Desktop>cd nombredelentorno\Scripts
c:\Desktop\nombredelentorno\Scripts>activate
(nombredelentorno) c:\Desktop\nombredelentorno\Scripts> y eso es todo
```
## Instalacion de los requirimientos

hay que instalar las librerias que se usa en el projecto, una vez tengamos el entorno virutal activado

```bash
(nombredelentorno) c:\Desktop\SistemaGestionPedidos>pip install -r requirements.txt
```
## Instalacion de la base de datos el projecto

crea una base de datos y luego modifica [DATABASES](https://github.com/TryNeo/sistema-gestion-pedidos/blob/master/SistemaGestionPedidos/settings.py)
para que se conecte a ese bd y a tu configuracion 
```bash
create database bd_gestion;
```

## Migracion de las tablas al BD del projecto
```bash
>>python manage.py makemigrations
>>python manage.py migrate
>>python manage.py runserver
```

