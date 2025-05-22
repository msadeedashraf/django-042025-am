from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required

# from . import forms


# Create your views here.
def blog(request):
    blog = Blog.objects.all().order_by("-date")
    return render(request, "blogs.html", {"blog": blog})


def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blogs_details.html", {"blog": blog})


@login_required(login_url="/users/login/")
def blog_new(request):
    # form = forms.CreateBlog()
    return render(request, "blog_new.html")


"""
def blog_page(request, slug):
    return HttpResponse(slug)
"""
