from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def joblisting(request):
    return render(request, "joblisting.html")


def jobsearch(request):
    return render(request, "jobsearch.html")


def privacy(request):
    return render(request, "privacy.html")


def terms(request):
    return render(request, "terms.html")
