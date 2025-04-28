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
 
from . import views
 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage ),
    path("contact/", views.contact ),
 
]
 
test the app
 
http://127.0.0.1:8000/

http://127.0.0.1:8000/contact/

### Making the  pages and static files work
 
Create folders (static and templates) in the root myproject folder

In static create css and scripts folder and place a styles.css and myscript.js file respectively.

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
<script src="{% static 'js/myscript.js' %}"></script>
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

