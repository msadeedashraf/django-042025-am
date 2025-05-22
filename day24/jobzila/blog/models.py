# Model field reference
# https://docs.djangoproject.com/en/5.2/ref/models/fields/

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    # author = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="Admin")
    banner = models.ImageField(default="default.jpg", blank=True, null=True)

    def __str__(self):
        return self.title
