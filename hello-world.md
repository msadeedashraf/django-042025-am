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
