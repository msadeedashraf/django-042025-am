from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=90)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    salaryrange = models.CharField(max_length=200)
    jobtype = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    applylink = models.URLField()
    postdate = models.DateTimeField(auto_now_add=True)
    expirydate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
