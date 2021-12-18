from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("login_page", views.login_page, name='login_page'),
    path("user_home", views.user_home,name='user_home'),
    path("sign_up", views.sign_up, name='sign_up'),
    path("logout_user", views.logout_user, name='logout_user'),
]
