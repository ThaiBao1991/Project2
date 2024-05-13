from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200,null=True)
    Author=models.CharField(max_length=200,null=True)
    Price=models.IntegerField()
    Edition=models.IntegerField()
 
    def __str__(self):
        return str(self.title)
 
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # Liên kết 1-1 với User khóa ngoại
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)
 
class Cart(models.Model): 
    customer=models.OneToOneField(Customer, null=True, on_delete=models.CASCADE) # Liên kết 1-1 Tới bảng customer khóa ngoại
    books=models.ManyToManyField(Book) # Liên kết Many-Many tới trường book, khóa ngoại
 
    def __str__(self):
        return str(self.customer)