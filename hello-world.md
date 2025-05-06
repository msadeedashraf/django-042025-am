>mkdir hello-world

>cd hello-world

>py -m venv .venv

>.\.venv\Scripts\Activate.ps1

>pip install Django

>django-admin startproject myproject

>cd myproject

>py .\manage.py runserver

Test 

>http://127.0.0.1:8000/
 
### Making the  urls work

create views.py in myproject folder and copy the following code
 
from django.http import HttpResponse
 
 
def homepage(request):
   return HttpResponse("Hello World!")
 
 
def contact(request):
   return HttpResponse("Our Contact Page")
 
 
update the urls.py file in myproject folder and copy the following code/replace

urls.py
``` 
from . import views
 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage ),
    path("contact/", views.contact ),
 
]

```
 
test the app
 
http://127.0.0.1:8000/

http://127.0.0.1:8000/contact/

### Making the  pages and static files work
 
Create folders (static and templates) in the root myproject folder

Inside static folder create css and scripts folder and place a styles.css and myscript.js file respectively.

styles.css

```

h1
{
    color: blue;
}

body {

    background-color: beige;
}
```

myscript.js

```
alert("This is test js")
```


In the templates folder create contact.html and myfirst.html files

contact.html

```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>


</head>
<body>
    <h1>Contact Us</h1>
<p>Welcome to my first Django project!</p>
<p>Go to our <a href="/">Home</a> page.</p>





</body>
</html>

```

myfirst.html

```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>

</head>
<body>
    <h1>Home Page</h1>
<p>Welcome to my first Django project!</p>
<p>Go to our <a href="/contact">Contact</a> page.</p>
</body>
</html>


```

Update the views.py file with the following code

views.py
```
from django.shortcuts import render

def homepage(request):
    return render(request, "myfirst.html")


def contact(request):
    return render(request, "contact.html")


```
Go to myproject\settings.py

add "DIRS": ["templates"]

```

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

```


test the app both urls should work
 
http://127.0.0.1:8000/


to add css and js files to the project

to add css 
```
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

to add javascript
```
<script src="{% static 'scripts/myscript.js' %}"></script>
```

on top of each .html page add the following code to load static files

```
{% load static %}
```

Go to myproject\settings.py

at the start add  import os

```
import os
from pathlib import Path
...
```



add STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

```
...
STATIC_URL = "static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
...
```
### Creating Blog App--Day08

(.venv) PS D:\CBC\django\day08\jobzila> py .\manage.py startapp blog

```
py .\manage.py startapp blog

```

```
> cd blog

> mkdir templates
```

create a blogs.html in the templates folder 
```
{% extends 'sharedpage.html'%}
{% block title %} Blog {% endblock title %}
{% block main %}
    <main>
        <section id="joblist-section">
            <h2>Blogs</h2>
            
        
            <div class="joblisting-div">
                <div class="job-listing">
                    <h3><a href="">Title of the Blog</a></h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae, perspiciatis?</p>
                    <p> 2025/04/30 by <strong>Sadeed</strong>  </p>
                    <p class="learn-more"><a href="#">Read More</a></p>


                </div>

            </div>     
        </section>
    </main>
{% endblock main %}
```



update the blog\views.py file
```
from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, "blogs.html")

```

create the blog\urls.py file 

```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog),
]

```

Go to myproject\settings.py and INSTALLED_APPS = []
```
[
    ...
    "django.contrib.staticfiles",
    "blog",
]
```

Go to myproject\urls.py and make sure to check include is imported  

```
...
from django.urls import path, include
...

urlpatterns = [
   ...
    path("blog/", include("blog.urls")),
]
```

run the project 
```
>py .\manage.py runserver 8005

```

Test the blog app using the url----http://127.0.0.1:8005/blog/


### Models & Migrations --Day09

Go to the blog\models.py and up the code [link](https://www.w3schools.com/django/django_models.php) 

```

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    link = models.URLField()
    date = models.DateTimeField()
    author = models.CharField(max_length=50)
    banner = models.ImageField()

```

> python -m pip install Pillow

# anytime a model is updated issue 

> py .\manage.py makemigrations 

# then to update the DB

> py .\manage.py migrate

optional to view the sql generated to create a table in the DB.

> python manage.py sqlmigrate blog 0001
 

### ORM ---Day 10

py .\manage.py shell

>>> from blog.models import Blog
>>> b = Blog() 
>>> b.title = "My Third Blog"
>>> b.body = "My Third Blog"
>>> b.slug = "My Third Blog"
>>> b.link = "My Third Blog"
>>> b.author = "My Third Blog"
>>> b.save()
>>> Blog.objects.all()


### Admin panel ---Day 11


> python manage.py createsuperuser

provide usename and password

To Check the login 

http://127.0.0.1:8000/admin/

To Delete the user 

> python manage.py shell

Inside the shell, run : 

>>>from django.contrib.auth.models import User
>>>User.objects.get(username='admin').delete()
>>>exit()

To Filter a user if it exist
>>>User.objects.filter(username='admin')

How to register the model in the admin panel 

Go to blog\admin.py
```
from .models import Blog

# Register your models here.

admin.site.register(Blog)
```

Try updating and Saving the data from the admin panel.

Now Connect the data on the blog Page


Go to blog\views.py
```
from .models import Blog

# Create your views here.
def blog(request):
    blog = Blog.objects.all().order_by("-date")
    return render(request, "blogs.html", {"blog": blog})

```


Go to blog\templates\blogs.html and update the following code
```
 <main>
        <section id="joblist-section">
            <h2>Blogs</h2>
            
            <div class="joblisting-div">

                {%  for b in blog  %}

                <div class="job-listing">
                    <h3><a href="">{{b.title}}</a></h3>
                    <p>{{b.body}}</p>
                    <p> {{b.date}} by <strong>{{b.author}}</strong>  </p>
                    <p class="learn-more"><a href="#">Read More</a></p>


                </div>
                {% endfor %}


            </div>     
        </section>
    </main>
```

### URL and Slugs ---Day 12

```
urlpatterns = [
    path("", views.blog, name="bloglist"),
]
```

```
  <li><a href="{% url 'bloglist' %}">Blog</a></li>
```

[Path Converters](https://docs.djangoproject.com/en/5.1/topics/http/urls/)