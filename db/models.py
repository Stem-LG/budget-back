from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField(default="",blank=True)
    manager = models.ForeignKey(User,on_delete=models.CASCADE, related_name='events')



class Fund(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='funds')
    source = models.ForeignKey(User,on_delete=models.CASCADE, related_name='funds')
    returnable = models.BooleanField(default=False)
        
    
    
class Expense(models.Model):

    item = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    invoice = models.TextField(default="",blank=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='expenses')
    spender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='expenses')

        
class Earning(models.Model):

    item = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='earnings')
    seller = models.ForeignKey(User,on_delete=models.CASCADE, related_name='earnings')
