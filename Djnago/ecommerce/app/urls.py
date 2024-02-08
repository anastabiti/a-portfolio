from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("auth", views.post_auth),
    path("user", views.create_user),
]