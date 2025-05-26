from django.shortcuts import render


# Create your views here.
def jobs(request):
    return render(request, "joblisting.html")


def job_new(request):
    return render(request, "job_new.html")
