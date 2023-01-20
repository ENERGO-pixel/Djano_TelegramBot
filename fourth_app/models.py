
from django.db import models
# Create your models here.
class Gym(models.Model):
    starttime = models.TimeField(auto_now=False, blank=True, null=True)
    endtime = models.TimeField(auto_now=False,blank=True,null=True)
    userid=models.PositiveBigIntegerField(default=1)
    # def save(self,*args,**kwargs):
    #     if self.starttime>self.endtime:
    #         self.endtime=self.starttime
    #     else:
    #         pass
    #     super(Gym,self).save(*args,**kwargs)
class Catagory(models.Model):
    name = models.CharField(null=False, max_length=100)
    def __str__(self):
        return self.name
class Products(models.Model):
    name = models.CharField(max_length=100, null=False)
    catagoryid=models.ForeignKey(Catagory,on_delete=models.CASCADE, null=True)
    price=models.DecimalField(decimal_places=2, max_digits=10, default=1)
    def __str__(self):
        return self.name
class Order(models.Model):
    date = models.DateTimeField()
    userid=models.PositiveBigIntegerField()
    productid=models.ForeignKey(Products,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.productid
class Trainer(models.Model):
    name=models.CharField(max_length=100, null=False)

class TrainWithTrainer(models.Model):
    nameid=models.ForeignKey(Trainer,on_delete=models.CASCADE, null=True)
    starttime = models.TimeField(auto_now=False, blank=True, null=True)
    endtime = models.TimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.nameid
class Subscription(models.Model):
    userid = models.PositiveBigIntegerField(default=1)
    name = models.CharField(max_length=100, null=False,default='day')
    price=models.DecimalField(decimal_places=2, max_digits=10, default=1)
    def __str__(self):
        return self.name
class Wallet(models.Model):
    userid = models.PositiveBigIntegerField(unique=True)
    balance=models.DecimalField(decimal_places=2, max_digits=100, default=0)
    def __str__(self):
        return str(self.userid)