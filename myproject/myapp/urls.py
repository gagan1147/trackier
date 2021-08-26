
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import home,login_view,logout_view,registration_view,add_user,contact_view_api,search_view
urlpatterns = [
    path('',home,name="home"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('registration/',registration_view,name='registration'),
    path('adduser/',add_user,name="addUser"),
    path('api/contacts/',contact_view_api,name="contacts"),
    path('api/search/',search_view,name="searchApi")
]
