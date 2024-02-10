from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("auth", views.login_),
    path("signup", views.create_user),
    path("auth/logout", views.logout_),
    # path("user", views.create_user),
]