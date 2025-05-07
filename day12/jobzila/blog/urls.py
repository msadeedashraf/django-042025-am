from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path("", views.blog, name="bloglist"),
    path("<slug:slug>", views.blog_page, name="blogpage"),
]
