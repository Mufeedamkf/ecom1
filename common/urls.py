from django.urls import path
from . import views

app_name='common'

urlpatterns=[
    path('',views.home,name='home'),
    path('master',views.master,name='master'),
    path('seller_sign',views.seller_sign,name='seller_sign'),
    path('seller_log',views.seller_log,name='seller_log'),
    path('customer_sign',views.customer_sign,name='customer_sign'),
    path('customer_log',views.customer_log,name='customer_log'),



    
    
    
]