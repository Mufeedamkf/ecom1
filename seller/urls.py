from django.urls import path
from . import views

app_name='seller'

urlpatterns=[
    path('home',views.home,name='home'),
    path('addproduct',views.addproduct,name='add_product'),
    path('master',views.master,name='master'),
]