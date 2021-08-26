

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
def home(request):
    
    try:
        if (request.user.is_authenticated):
            contact = Contacts.objects.filter(user = request.user)
            context = {
                "contacts":contact
            }
        return render(request,'home.html',context)
    except:
        form =  AuthenticationForm(request,data=request.POST or None)
        if form.is_valid():
            user_ = form.get_user()
            login(request,user_)
            return redirect("/")
        context = {"form":form}
        return render(request,'components/auth/login.html',{"form":form})

def contact_view_api(request):
    contexts = {}
    contexts['Contacts'] = []
    if (request.user.is_authenticated):
        contacts = Contacts.objects.filter(user=request.user)
        for contact in contacts:
            jsontype = {
                "firstName":contact.firstName,
                "lastName":contact.lastName,
                "email":contact.email,
                "mobile":contact.mobileNumber
            }
            contexts["Contacts"].append(jsontype)
    return JsonResponse(contexts)


def search_view(request):
    contexts = {}
    contexts['Contacts'] = []
    print(request.GET.get("searchValue"))
    if(request.GET):
        searchValue = request.GET.get("searchValue") 
        try:
            searchValue = int(searchValue)
            contacts = Contacts.objects.filter(mobileNumber__icontains=searchValue,user= request.user)
            for contact in contacts:
                jsontype = {
                    "firstName":contact.firstName,
                    "lastName":contact.lastName,
                    "email":contact.email,
                    "mobile":contact.mobileNumber
                }
                contexts["Contacts"].append(jsontype)
        except:
            contacts = Contacts.objects.filter(firstName__icontains=searchValue,user= request.user)
            for contact in contacts:
                jsontype = {
                    "firstName":contact.firstName,
                    "lastName":contact.lastName,
                    "email":contact.email,
                    "mobile":contact.mobileNumber
                }
                contexts["Contacts"].append(jsontype)
    return JsonResponse(contexts)

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