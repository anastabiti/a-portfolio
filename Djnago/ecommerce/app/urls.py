from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("auth", views.login_),
    path("auth/logout", views.logout_),
    path("user", views.create_user),
]