from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


# Create your views here.
def blog(request):
    blog = Blog.objects.all().order_by("-date")
    return render(request, "blogs.html", {"blog": blog})


def blog_page(request, slug):
    return HttpResponse(slug)
