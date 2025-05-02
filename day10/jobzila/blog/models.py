# Model field reference
# https://docs.djangoproject.com/en/5.2/ref/models/fields/

from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    banner = models.ImageField()

    def __str__(self):
        return self.title


"""
http://127.0.0.1:8006/blog/title-of-the-blog
http://127.0.0.1:8006/blog/finding-a-job-as-new-grad
http://127.0.0.1:8006/blog/how-to-search-job

slug -- title-of-the-blog
slug -- finding-a-job-as-new-grad
slug -- how-to-search-job

"""
