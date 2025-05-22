from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
from . import forms

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
    if request.method == "POST":
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            # save logic
            # form.save()
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("blogapp:bloglist")
    else:
        form = forms.CreateBlog()

    return render(request, "blog_new.html", {"form": form})


"""
def blog_page(request, slug):
    return HttpResponse(slug)
"""
