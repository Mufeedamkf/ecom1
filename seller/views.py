from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'seller/home.html')

def addproduct(request):
    return render(request,'seller/addproduct.html')

def master(request):
    return render(request,'seller/master.html')

