# Django Site

## Packages

### Global Environment

- Python 3.7.3
- virtualenv 6.6.0
- pylint
- autopep8
- flake8

### Virtual Environment

- Django 2.2.2
- pillow

## Commands

- Start project

```shell
django-admin startproject config .
```

- Run server

```shell
python manage.py runserver <ip:port>
```

- Migration

```shell
python manage.py makemigrations
python manage.py migrate
```

- Create Super User

```shell
python manage.py createsupersuser
<username>
<emaill>
<possword>
<re-password>
```

- Create a New App

```shell
python manage.py startapp core
```
