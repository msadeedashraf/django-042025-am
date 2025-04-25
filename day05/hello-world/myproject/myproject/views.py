# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello World!")
    return render(request, "myfirst.html")


def contact(request):
    # return HttpResponse("Our Contact Page")
    return render(request, "contact.html")
