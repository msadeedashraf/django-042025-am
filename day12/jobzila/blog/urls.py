from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="bloglist"),
    path("<slug:slug>", views.blog_page, name="blogpage"),
]
