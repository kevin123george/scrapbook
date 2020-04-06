from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print("form is valid")
            form.save()

        else:
            print(response.POST)

        return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


def home(request):
    return render(request, 'home.html')
