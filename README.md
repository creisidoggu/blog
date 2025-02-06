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
To start a local server, use this command:

```bash
python path_to_your_manage.py runserver
```

In addition to starting the server, this command automatically creates an SQLite database (db.sqlite3) in the project folder.

## URLs & Views

When a browser makes a request to a URL on your Django website (e.g., '/about'), Django performs the following steps:

1. **Check the `urls.py`**: Django examines this file to determine which URL is being requested.
2. **Decides which function to execute in `views.py`**: Based on the URL, Django selects the appropriate function to handle the request.
3. **Renders the response in the browser**: Whatever is executed in `views.py` will be displayed to the user in the browser (e.g., the content of an "About" page).


> **Note**: When creating a project, Django automatically generates a `urls.py`, file, but it does not create a `views.py` file. This file must be created manually when needed.
