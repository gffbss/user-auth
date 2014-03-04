# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from auth.forms import UserForm, SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
            return redirect("/home")

    else:
        form = SignUpForm()
    data = {'form': form}
    return render(request, "signup.html", data)

def home(request):
    return render(request, "index.html")