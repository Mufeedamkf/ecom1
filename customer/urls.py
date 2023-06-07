from django.urls import path
from . import views

app_name='customer'

urlpatterns=[
    path('master',views.master,name='master'),
    path('home',views.home,name='home'),


]