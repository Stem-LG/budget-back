from django.db import models

# Create your models here.
    
class Person(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(default="",blank=True)
    description = models.TextField(default="",blank=True)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    description = models.TextField(default="",blank=True)
    manager = models.ForeignKey(Person,on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name
    
class Fund(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='funds')
    source = models.ForeignKey(Person,on_delete=models.CASCADE, related_name='funds')
    returnable = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Expense(models.Model):

    item = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    invoice = models.TextField(default="",blank=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='expenses')
    spender = models.ForeignKey(Person,on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return self.item
    
class Earning(models.Model):

    item = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='earnings')
    seller = models.ForeignKey(Person,on_delete=models.CASCADE, related_name='earnings')

    def __str__(self):
        return self.item