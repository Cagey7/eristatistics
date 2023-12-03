# eristatistics RESTful API

## Setup with development settings

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Cagey7/eristatistics.git
$ cd eristatistics
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ .\venv\Scripts\activate
```

Then install the dependencies:

```sh
(venv) $ pip install -r .\requirements\local.txt
```

Then edit eristatistics/settings/local.py with your database settings.

Make migrations:

```sh
(venv) $ python manage.py makemigrations --settings=eristatistics.settings.local
(venv) $ python manage.py migrate --settings=eristatistics.settings.local
```

Run server:

```sh
(venv) $ python manage.py runserver --settings=eristatistics.settings.local
```
