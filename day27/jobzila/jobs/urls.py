from django.urls import path, include
from . import views

app_name = "jobapp"

urlpatterns = [
    path("", views.jobs, name="joblist"),
    path("new-job/", views.job_new, name="new-job"),
]
