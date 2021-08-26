

from django.conf import settings

from .models import Contacts
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.utils.http import is_safe_url

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# Create your views here.
from django.contrib.auth.models import User
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
# Create your views here.

def login_view(request):
    form =  AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return redirect("/")
    context = {"form":form}
    return render(request,"components/auth/login.html",context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    context = {
        "form":None
    }
    return render(request,"components/auth/logout.html",context)

def registration_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request,user)
        return redirect("/")
    context = {"form":form }
    return render(request,"components/auth/registration.html",context)