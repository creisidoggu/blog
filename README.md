# 🐍 Django Blog Creation Practice 📝

## 1️⃣ Project Creation & Initialization 🚀

To install Django 🏗️, first prepare the working environment 🖥️ and then run:

```bash
pip install django
```

To create the project 📂:

```bash
django-admin startproject project_name
```

To start a local server 🌍, run inside the project folder:

```bash
cd project_name
python manage.py runserver
```

This command also creates an SQLite database 🗄️ (`db.sqlite3`).

---

## 2️⃣ URLs & Views 🔗👀

When a browser 🌐 requests a URL (e.g., `/about`), Django follows these steps:

1️⃣ **Checks `urls.py` 📜**: Determines which view will handle the request.
2️⃣ **Executes `views.py` ⚡**: Selects the appropriate function.
3️⃣ **Renders response 📺**: Displays the content in the browser.

> ⚠️ **Note**: Django creates `urls.py` automatically, but `views.py` must be manually created.

---

## 3️⃣ Creating an Application ⚙️

To create an app 🏛️ inside the Django project:

```bash
django-admin startapp app_name
```

> 💡 **Note**: An app is a functionality within the project. Example: an authentication system 🔑 or a blog posts CRUD 📝.

---

## 4️⃣ Migrations 📦

To reflect model changes in the database 💾, generate migration files:

```bash
python manage.py makemigrations
```

> ⚠️ **Note**: Ensure the app is added to `INSTALLED_APPS` in `settings.py` ⚙️, or changes won’t be detected.

Then, apply migrations:

```bash
python manage.py migrate
```

---

## 5️⃣ ORM (Object-Relational Mapping) 🗃️

To access Django's interactive shell 🖥️:

```bash
python manage.py shell
```

Inside the shell, import models 📜 and perform queries. Example with `Post`:

```python
from post.models import Post
```

List all objects 📋:

```python
Post.objects.all()
```

Create an instance 🆕:

```python
post = Post(title="My first post", content="This is the content")
post.save()
```

> ⚠️ **Note**: Unlike plain Python 🐍, you must execute `.save()` to store the instance in the database.

---

## 6️⃣ Admin Section 🎛️

To access Django’s admin interface (`/admin`), create a superuser 👤:

```bash
python manage.py createsuperuser
```

To add models 📜 to the admin interface, edit `admin.py` and register the models:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

> ⚠️ **Note**: If the model doesn’t display correctly in the admin panel, ensure the `__str__` method is defined in the model class.

---

## 7️⃣ Template Tag System 🎨

Django uses a template system to dynamically generate HTML pages. In a template file, the `{% ... %}` and `{{ ... }}` syntax is used:

- `{% for post in posts %} ... {% endfor %}`: Loop through a list of objects.
- `{{ post.title }}`: Insert dynamic content into the page.

Example of a Django template rendering a list of posts:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Posts</title>
</head>
<body>
    <h1>Posts</h1>
    <div class="posts">
        <!-- Loop through posts -->
        {% for post in posts %}
            <div class="post">
                <!-- Display post details -->
                <h2><a href="#">{{ post.title }}</a></h2>
                <p>{{ post.body }}</p>
                <p>{{ post.date }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

This template will generate an HTML page listing all posts stored in the database dynamically.