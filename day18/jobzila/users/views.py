from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("blogapp:bloglist")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        # return redirect("users:login")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # logic here
            login(request, form.get_user())

            return redirect("blogapp:bloglist")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
