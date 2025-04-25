from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello World!")


def contact(request):
    return HttpResponse("Our Contact Page")
