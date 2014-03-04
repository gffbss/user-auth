# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from auth.forms import SignUpForm, LoginForm


def index(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "special.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
            return redirect("/special")

    else:
        form = SignUpForm()
    data = {'form': form}
    return render(request, "signup.html", data)

# The decorator helps authenticate users in a DRY way
@login_required
def special_page(request):
    data = {}
    return render(request, "special.html", data)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                print 'We got to here'
                if user.is_active:
                    login(request, user)
                    return redirect("/secret")
                else:
                    return 'Invalid Account'
    else:
        form = LoginForm()

    data = {'form': form}
    return render(request, "login.html", data)