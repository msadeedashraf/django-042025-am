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

```
urlpatterns = [
    path("", views.blog, name="bloglist"),
    path("<slug:slug>", views.blog_page, name="blogpage"),
]

```

```
from django.http import HttpResponse

def blog_page(request, slug):
    return HttpResponse(slug)

```

blog/templates/blogs.html
```

                {%  for b in blog  %}

                <div class="job-listing">
                    <h3><a href="{% url 'blogpage' slug=b.slug %}">{{b.title}}</a></h3>
                    <p>{{b.body}}</p>
                    <p> {{b.date}} by <strong>{{b.author}}</strong>  </p>
                    <p class="learn-more"><a href="#">Read More</a></p>


                </div>
                {% endfor %}
```

Change the URLs to app the app_name in blog\urls.py
```
app_name = "blogapp"

urlpatterns = [
    path("", views.blog, name="bloglist"),
    path("<slug:slug>", views.blog_page, name="blogpage"),
]


```

Update the blog\blogs.html
```
    {%  for b in blog  %}

                <div class="job-listing">
                    <h3><a href="{% url 'blogapp:blogpage' slug=b.slug %}">{{b.title}}</a></h3>
                    <p>{{b.body}}</p>
                    <p> {{b.date}} by <strong>{{b.author}}</strong>  </p>
                    <p class="learn-more"><a href="#">Read More</a></p>


                </div>
                {% endfor %}
```

Update the url in the sharedpage.html as well
```
<nav>
        <ul>
          <li><a href="../">Home</a></li>
          <li><a href="../jobsearch">Job Search</a></li>
          <li><a href="../joblisting">Job Listing</a></li>
          <li><a href="../terms">Terms of Service</a></li>
          <li><a href="../privacy">Privacy Policy</a></li>
          <li><a href="../contact">Contact Us</a></li>
          <li><a href="../contact">Contact Us</a></li>
          <li><a href="{% url 'blogapp:bloglist' %}">Blog</a></li>

          <li><a href="../addjobs">Add Job</a></li>


        </ul>
```

Create a blogs_details.html page in the blog\templates folder

blogs_details.html
```
{% extends 'sharedpage.html'%}
{% block title %} Blog {% endblock title %}
{% block main %}
    <main>
        <section id="joblist-section">
            <h2>{{blog.title}}</h2>
            
            <div class="joblisting-div">

                 <div class="job-listing">
                    <p>{{blog.body}}</p>
                    <p> {{blog.date}} by <strong>{{blog.author}}</strong>  </p>
                    <p class="learn-more"><a href="#">Read More</a></p>


                </div>
                

            </div>     
        </section>
    </main>
{% endblock main %}
  

```

Update the blog\views.py by replace the blog_page with the following code
```

def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blogs_details.html", {"blog": blog})
```

Now To Upload images in the Blog Posts add the following in the settings.py file
```
MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

myproject/urls.py
```
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage),
    path("joblisting/", views.joblisting),
    path("contact/", views.contact),
    path("jobsearch/", views.jobsearch),
    path("privacy/", views.privacy),
    path("terms/", views.terms),
    path("blog/", include("blog.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


```

Check and Install the Package

>pip show pillow
>pip install pillow


in the models.py update the banner to hold the default image
```
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    banner = models.ImageField(default="default.jpg", blank=True, null=True)

```

the model is changed 

>py .\manage.py makemigrations
>py .\manage.py migrate

Test the app
http://127.0.0.1:8000/admin/blog/

### Day 16 -- User Registration

#### Django Forms

[Forms](https://docs.djangoproject.com/en/5.1/ref/forms/)

[Working with forms](https://docs.djangoproject.com/en/5.1/topics/forms/)

[](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/)

[Using the Django authentication system](https://docs.djangoproject.com/en/5.2/topics/auth/default/)

[Django Tutorial Part 9: Working with forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Forms)

#### How to use Django’s CSRF protection
[How to use Django’s CSRF protection](https://docs.djangoproject.com/en/5.1/howto/csrf/)

[Cross Site Request Forgery protection](https://docs.djangoproject.com/en/5.2/ref/csrf/)


(.venv) PS D:\CBC\django\day16\jobzila> py .\manage.py startapp users

```
py .\manage.py startapp users

```

add users/urls.py in the users app folder
```
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [path("register/", views.register_view, name="register")]

```


update the users/views.py
```
def register_view(request):
    return render(request, "register.html")

```

create users/templates/register.html
```
{% extends 'sharedpage.html'%}
{% block title %} Register User {% endblock title %}
{% block main %}
    <main>
        <section id="joblist-section">
            <h2>Register a New User</h2>
            
            </div>     
        </section>
    </main>
{% endblock main %}
  

```

Test the app 
> py .\manage.py runserver

http://127.0.0.1:8000/users/register/

and check the newly created register.html page in response

### Day 18 --- Login and Authentication

sharedpage.html
```
...
          <li><a href="{% url 'users:register' %}">Register</a></li>
          <li><a href="{% url 'users:login' %}">Login</a></li>
          
          <li><a href="/addjobs">Add Job</a></li>
...
```

users\urls.py
```
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
]

```
users\views.py
```
...
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
...


def login_view(request):
    if request.method == "POST":
        return redirect("users:login")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


```

create users\templates\login.html
```

```

Test the app top see the login page with form

update users/views.py
```

def login_view(request):
    if request.method == "POST":
        # return redirect("users:login")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # logic here
            return redirect("blogapp:bloglist")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

```

Test
http://127.0.0.1:8000/users/login/

TO see if correct user/password redirects to the blog page successfully


users/views.py
```
...
from django.contrib.auth import login
...

def login_view(request):
    if request.method == "POST":
        # return redirect("users:login")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # logic here
            login(request, form.get_user())

            return redirect("blogapp:bloglist")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

```

Test the app for not allowing to access the admin page if logged in from the app as a non-admin user.
http://127.0.0.1:8000/users/login/
http://127.0.0.1:8000/admin/


### Day 19 --- Authorization

users/urls.py
```
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

```

users/views.py
```
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("blogapp:bloglist")

```


jobzila/templates/sharedpage.html
```
 <nav>
        <div class="menu-container">
           <!-- Hamburger icon -->
        <div class="hamburger" onclick="toggleMenu()">
          <span></span>
          <span></span>
          <span></span>
      </div>

      <!-- Navigation links -->
        <ul id="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/jobsearch">Job Search</a></li>
          <li><a href="/joblisting">Job Listing</a></li>
          <li><a href="/terms">Terms of Service</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/contact">Contact Us</a></li>
          <li><a href="/contact">Contact Us</a></li>
          <li><a href="{% url 'blogapp:bloglist' %}">Blog</a></li>
          <li><a href="/addjobs">Add Job</a></li>
          
        
          
<div class="right-align" >

        <form method="POST" class="logout" action="{% url 'users:logout' %}">
              {% csrf_token %}
                <button class="logout-button" >Logout</button>
              </form>

          <li><a href="{% url 'users:register' %}">Register</a></li>

          <li><a href="{% url 'users:login' %}">Login</a></li>

</div>
         </ul>
      </div>
      </nav>
```

Get rid of all the previous nav styles and add the following in css/styles.css
```
/* NAV Start Here*/

nav {

    background-color: #ff8500;
    color: #fff;
    padding: 10px;
}

nav ul {
list-style: none;
margin:0;
padding: 0;
display: flex;
justify-content: flex-start;
align-items: center;
}

nav ul li {

    margin-right: 20px;
}
nav ul .right-align 
{

  margin-left: auto;
  display: flex;
  align-items: center;

}

nav ul li a {
    color: white;
    text-decoration: none;
}

nav ul .logout 
{
  margin-left: auto;
}

.logout-button
{
 font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
 border: none;
 background: none  ;
 color: white;


}
nav ul li a:hover {
    color: #fbe3d3;
    
}


/* Hamburger menu icon */
.hamburger {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.hamburger span {
  height: 3px;
  width: 25px;
  background-color: white;
  margin: 5px 0;
  transition: 0.4s;
}

/* Responsive - hide menu links initially */
#nav-links {
  display: flex;
  flex-direction: row;
}

#nav-links li {
  display: block;
}

/* For smaller screens */
@media (max-width: 768px) {
  .hamburger {
      display: flex;
  }

  #nav-links {
      display: none;
      flex-direction: column;
      width: 100%;
      background-color: #333;
      position: absolute;
      top: 60px;
      left: 0;
  }

  #nav-links li {
      width: 100%;
      text-align: center;
  }

  #nav-links.show {
      display: flex;
  }
}

/* Nav ends here*/

```

### Day 20 ---Authorisation

blog/urls.py
```
urlpatterns = [
    path("", views.blog, name="bloglist"),
    path("new-blog/", views.blog_new, name="new-blog"),
    path("<slug:slug>", views.blog_page, name="blogpage"),
]
```

blog/views.py
```

@login_required(login_url="/users/login/")
def blog_new(request):
    # form = forms.CreateBlog()
    return render(request, "blog_new.html")

```

create blog/templates/blog_new.html
```
{% extends 'sharedpage.html'%}
{% block title %} Add Blog {% endblock title %}
{% block main %}
    <main>
       <section id="login-form-section">
  
  <h2>New Blog</h2> 
  <div class="form-div">
        <form class="" id="contact-form" action="{% url 'blogapp:new-blog'%}" method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          {{form}}        
          <button>Add Blog</button>
</form>



        </div>

       
            

      
    </div>
  </section>
    </main>
{% endblock main %}
  

```
-Test the code

### Day 22 

- To implement the custom nav based on the user logged in 

templates/sharedpage.html
```
    <ul id="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/jobsearch">Job Search</a></li>
          <li><a href="/joblisting">Job Listing</a></li>
          <li><a href="/terms">Terms of Service</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/contact">Contact Us</a></li>         
          
          <li><a href="{% url 'blogapp:bloglist' %}">Blog</a></li>
          
          {% if user.is_authenticated  %}


          <li><a href="{% url 'blogapp:new-blog' %}">Add Blog</a></li>
          <li><a href="/addjobs">Add Job</a></li>
          

          {% endif %}
          
        
          
<div class="right-align" >

  {% if user.is_authenticated %}
  <form method="POST" class="logout" action="{% url 'users:logout' %}">
              {% csrf_token %}
                <button class="logout-button" >Logout</button>
              </form>

  {% else %}
  <li><a href="{% url 'users:register' %}">Register</a></li>

          <li><a href="{% url 'users:login' %}">Login</a></li>


  {% endif %}

        

          
</div>
         </ul>
```

### Day 24 Custom Forms

