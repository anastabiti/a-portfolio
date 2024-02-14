from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("auth", views.login_),
    path("signup/seller", views.create_user),
    path("signup/buyer", views.create_user_buyer),
    path("auth/logout", views.logout_),
    path("products/list",views.list_product),
    path("products",views.all_products),
    path("users",views.get_all_user),
    path("upload",views.uploading),
    path("google",views.google_auth),
    path("google/callback",views.google_auth_callback),
    path("products/all",views.get_all_products),
    path("products/buy",views.buy),

    # path("user", views.create_user),
]