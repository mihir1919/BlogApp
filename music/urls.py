from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('accounts/profile/',views.profile,name="profile"),
    path('details/<int:pk>/', views.details,name="details"),
    path('add/',views.add,name="add"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('login/', LoginView.as_view(template_name="music/login.html"), name="login"),
    path('index/', LogoutView.as_view(template_name="music/index.html"),name="logout"),
    path('search/', views.search, name="search"),
]