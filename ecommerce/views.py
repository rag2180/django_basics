from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
#from django.contrib.auth.models import User


def home_page(request):
    context = {
        "title": "Home",
        "content": "Welcome to Home Page",
    }
    if request.user.is_authenticated():
        print("User is Authenticated...")
        context["premium_content"] = "Yeahhhh.....This is for logged in users only.\nYou are Logged in as - {}".format(request.user.username)
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Us",
        "content": "Welcome to About Page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us",
        "content": "Welcome to Contact Page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))  # Note: fullname is variable name in ContactForm class
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("User:{} Authentication - {}".format(user, request.user.is_authenticated()))
        if user is not None:
            login(request, user)
            context["form"] =LoginForm()
            # Redirect To Success Page
            return redirect("/")
        else:
            print("Error")

    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, password, email)
        user.save()
        print("New User Created - {}".format(user))
    return render(request, "auth/register.html", context)
