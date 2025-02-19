# Django Blog Creation Practise

## Project Creation and Initialization

To install Django within a project, after preparing the working environment, use the following command:

```bash
pip install django
```

To create the project itself, run the following command:

```bash
django-admin startproject project_name
```
To start a local server, use this command over the created folder with the same name as the project_name:

```bash
cd project_name
python path_to_your_manage.py runserver
```

In addition to starting the server, this command automatically creates an SQLite database (db.sqlite3) in the project folder.

## URLs & Views

When a browser makes a request to a URL on your Django website (e.g., '/about'), Django performs the following steps:

1. **Check the `urls.py`**: Django examines this file to determine which URL is being requested.
2. **Decides which function to execute in `views.py`**: Based on the URL, Django selects the appropriate function to handle the request.
3. **Renders the response in the browser**: Whatever is executed in `views.py` will be displayed to the user in the browser (e.g., the content of an "About" page).


> **Note**: When creating a project, Django automatically generates a `urls.py`, file, but it does not create a `views.py` file. This file must be created manually when needed.

## Creating an App

Whith the following command you can create an app: 

```bash
django-admin startapp app_name
```

> **Note**: This thing is a functionality of the project, for example an authentification system would be an app for the django project, an Posts CRUD for a blog could be a good example for an app functionality.

## Migration

We have to do a migration file to migrate the models to the database, to make the migrations we should put

```bash
python manage.py makemigrations
```

> **Note**: Remember that u have to put the app on the settings.py main file or wouldn't detect the changes on the model

And then to apply the migrations we should use

```bash
python manage.py migrate
```

## ORM

To enter the terminal of our database we enter the next command:

```bash
python manage.py shell
```

On the shell we could create a table like i created the Post table with

```bash
from post.models import Post
```

After that we can see that Posts is a class __posts.models.Post__, we can see all the items with the following command:

```bash
Post.objects.all()
```

I we want to create an instance of an object is like in python (with the difference that after instancing u have to save it) and we can modify like in python.

## Admin section

When u go to the _/admin_ on the url u have to enter a login form, if u try to log in u don't have any user.

To create an superuser for us we have to enter:

```bash
python manage.py createsuperuser
```

U can add to the /admin section a model adding to the admin.py of the app the importation of the model
> **Note**: If you don't see properly the model u should put the str dunder on the class.