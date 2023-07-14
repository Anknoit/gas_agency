from django.urls import path
from . import views #importing views from current package (. maeans current package)


urlpatterns = [
    path("", views.index, name='index'),
    path("handleLogin", views.handleLogin, name='login'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("signout", views.signout, name='signout'),
    path("customer_register", views.customer_register, name='customer_register'),
    path("new_order", views.new_order, name='new_order'),
    path("customer_list", views.customer_list, name='customer_list'),
    path("order_list", views.order_list, name='order_list'),
    path("agency_list", views.agency_list, name='agency_list')
]