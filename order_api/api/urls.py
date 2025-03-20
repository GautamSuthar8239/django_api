from django.urls import path
from .views import (
    register_user, login_user, get_users, get_user_profile, delete_user,
    get_orders, create_order, update_order, delete_order
)

urlpatterns = [
    # User authentication
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", get_user_profile, name="profile"),
    path('users/', get_users, name='get_users'),
    path("users/<int:user_id>/delete/", delete_user, name="delete-user"),

    # Order management
    path("orders/", get_orders, name="orders"),
    path("orders/create/", create_order, name="create-order"),
    path("orders/<int:order_id>/update/", update_order, name="update-order"),
    path("orders/<int:order_id>/delete/", delete_order, name="delete-order"),
]
