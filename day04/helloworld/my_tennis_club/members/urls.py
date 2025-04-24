from django.urls import path
from .migrations import views

urlpatterns = [
    path("members/", views.members, name="members"),
]
