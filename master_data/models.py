from django.db import models

# Create your models here.
class Supplier(models.Model):
    SupplierPk = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=255, unique=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.SupplierName


class Customer(models.Model):
    CustomerPk = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=255, unique=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.CustomerName


class Product(models.Model):
    ProductPk = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255, unique=True)
    QtyPcsPerDus = models.IntegerField(default=1)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ProductName


class Warehouse(models.Model):
    WhsPk = models.AutoField(primary_key=True)
    WhsName = models.CharField(max_length=255, unique=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.WhsName