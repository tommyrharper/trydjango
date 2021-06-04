# How To

- To open the virtual env

```
source bin/activate
```

- To exit the venv

```
deactivate
```

To see what you are running on python:

```
pip freeze
```

- To see where you are running python from:

```
which python
which python3
```

- To access django admin:

```
django-admin
```

- To start a new project

```
django-admin startproject trydjango .
```

- To run the server

```
python manage.py runserver
```

- To migrate the DB:
```
python manage.py migrate
```

- To create a super user:

```
python manage.py createsuperuser
```

- Create a new app:

```
python manage.py startapp app-name
```

- In order to make new migraitons:

```
python manage.py makemigrations
# then to execute them
python manage.py migrate
```