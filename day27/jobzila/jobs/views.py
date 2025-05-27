from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from . import forms


# Create your views here.
def jobs(request):
    jobs = Job.objects.all()
    return render(request, "joblisting.html", {"jobs": jobs})


@login_required(login_url="/users/login/")
def job_new(request):
    if request.method == "POST":
        form = forms.CreateJob(request.POST)
        if form.is_valid():
            # save the job
            newjob = form.save(commit=False)
            newjob.user = request.user
            newjob.save()
            return redirect("jobapp:joblist")
    else:
        form = forms.CreateJob()
    return render(request, "job_new.html", {"form": form})
