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

- To enter the python shell:

```
python manage.py shell
```

- Then to access an app model:

```
> form products.models import Product
> Product.objects.all()
> Product.objects.create(title='new product 2', description='another one', price='12341', summary='nice')
```
- To clear the DB and reset any changes:
  - Delete anything in your app `/migrations` folder **EXCEPT** the `__init__.py` file.
  - Then delete the `/migrations/__pycache__` folder.
  - Delete your db: `src/db.sqlite3`.

