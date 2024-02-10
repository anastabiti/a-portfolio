from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("auth", views.login_),
    path("signup/seller", views.create_user),
    path("signup/buyer", views.create_user_buyer),
    path("auth/logout", views.logout_),
    # path("user", views.create_user),
]