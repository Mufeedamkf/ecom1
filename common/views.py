
from django.shortcuts import render,redirect

from common.models import Seller
from common.models import Customer

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def master(request):
    return render(request,'common/master.html')

def seller_sign(request):
    
    msg=''
    if request.method == 'POST' :

        
        seller_name=request.POST['name']
        seller_add=request.POST['address']
        seller_mail=request.POST['email']
        seller_gender=request.POST['gender']
        seller_ph=request.POST['phone']
        seller_photo=request.FILES['photo']
        seller_company=request.POST['company']
        seller_acholder=request.POST['accountHolder']
        seller_acno=request.POST['accountno']
        seller_ifsc=request.POST['ifsc']
        seller_pw=request.POST['password']

        seller_exist=Seller.objects.filter(email=seller_mail).exists()

        if not seller_exist:
        
            seller=Seller(name=seller_name,
                              address=seller_add,
                              email=seller_mail,
                              gender=seller_gender,
                              phno=seller_ph,
                              photo= seller_photo,
                              company_name=seller_company,
                              ac_holder_name=seller_acholder,
                              ac_no=seller_acno,
                              ifsc=seller_ifsc,
                              password=seller_pw
                              )
            seller.save()
            msg='sign up success'

        else:
            msg='seller already exists'

    return render(request,'common/seller_sign.html',{'message':msg})

def seller_log(request):
    return render(request,'common/seller_log.html')

def customer_sign(request):

    msg=''
    if request.method == 'POST' :

        
        customer_name=request.POST['name']
        customer_add=request.POST['address']
        customer_mail=request.POST['email']
        customer_gender=request.POST['gender']
        customer_ph=request.POST['phone']
        customer_photo=request.FILES['photo']
        customer_company=request.POST['company']
        customer_acholder=request.POST['accountHolder']
        customer_acno=request.POST['accountno']
        customer_ifsc=request.POST['ifsc']
        customer_pw=request.POST['password']

        customer_exist=Customer.objects.filter(email=customer_mail).exists()

        if not customer_exist:
        
            customer=Customer(name=customer_name,
                              address=customer_add,
                              email=customer_mail,
                              gender=customer_gender,
                              phno=customer_ph,
                              photo=customer_photo,
                              company_name=customer_company,
                              ac_holder_name=customer_acholder,
                              ac_no=customer_acno,
                              ifsc=customer_ifsc,
                              password=customer_pw
                              )
            customer.save()
            msg='sign up success'

        else:
            msg='seller already exists'

    

    return render(request,'common/customer_sign.html',{'message':msg})

def customer_log(request):
    return render(request,'common/customer_log.html')





