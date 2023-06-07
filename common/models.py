from django.db import models

# Create your models here.


class Seller(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    phno=models.BigIntegerField(default=1)
    photo=models.ImageField(upload_to='seller/',default='')
    company_name=models.CharField(max_length=30)
    ac_holder_name=models.CharField(max_length=30,default='')
    ac_no=models.CharField(max_length=30,default='')
    ifsc=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=30,default='')
    

    class Meta:
        db_table = 'seller_tb'


class Customer(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    phno=models.BigIntegerField(default=1)
    photo=models.ImageField(upload_to='seller/',default='')
    company_name=models.CharField(max_length=30)
    ac_holder_name=models.CharField(max_length=30,default='')
    ac_no=models.CharField(max_length=30,default='')
    ifsc=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=30,default='')
    

    class Meta:
        db_table = 'customer_tb'


        