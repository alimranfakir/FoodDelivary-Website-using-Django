# Django Installation

### Creating a virtual environment

We need to create a virtual env for our app 
Run this command in whatever folder you want to create your venv folder

```
python -m venv practiceecom 
```
### 'practiceecom' is name of virtual env

### then enter the env
```
cd practiceecom
```


### Activate the virtualenv


```
# Windows
.\Scripts\Activate
```
### Check packages installed in that env

```
pip freeze
```

### Install Django

```
pip install django
```

### Create your project

```
django-admin startproject PROJECTNAME
```

### Run Server (http://127.0.0.1:8000) CTRL+C to stop

```
python manage.py runserver
```

### Create an app
```
python manage.py start app APPNAME
```

### Create migrations
```
python manage.py makemigrations
```

### Run migration
```
python manage.py migrate
```

### Collect Static Files
```
python manage.py collectstatic
```
