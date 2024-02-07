from django import forms
from .models import Supplier, Customer, Product, Warehouse

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['SupplierName']
        widgets = {
            'SupplierName': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['CustomerName']
        widgets = {
            'CustomerName': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['ProductName', 'QtyPcsPerDus']
        widgets = {
            'ProductName': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'QtyPcsPerDus': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['WhsName']
        widgets = {
            'WhsName': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }