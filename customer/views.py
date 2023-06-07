from django.shortcuts import render

# Create your views here.
def master(request):
     return render(request,'customer/master.html')

def home(request):
     return render(request,'customer/home.html')