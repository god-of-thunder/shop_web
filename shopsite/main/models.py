from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    time = models.DateTimeField(default=timezone.now)
    confirmed = models.IntegerField()
    account = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'users'

class Product(models.Model):
    title = models.CharField(max_length=2000,blank=True,null=True)
    srcset = models.CharField(max_length=1000)
    sold = models.IntegerField()
    money = models.IntegerField()
    sell = models.CharField(max_length=1000)
    id = models.IntegerField(primary_key=True)
    stock = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'product'

class Business(models.Model):
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    amount = models.IntegerField()
    total_price = models.IntegerField()
    product_id = models.IntegerField()
    transaction_time = models.DateTimeField()
    order_number = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'business'

class SystemConfig(models.Model):
    account = models.CharField(primary_key=True, max_length=100)
    key1 = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'system_config'

class Limitedtime(models.Model):
    seller = models.CharField(max_length=200)
    limitquantity = models.IntegerField()
    price = models.IntegerField()
    product_id = models.IntegerField()
    srcset = models.ImageField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'limitedtime'                       
