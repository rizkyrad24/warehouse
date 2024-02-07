from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, View, DeleteView
from .models import Supplier, Customer, Product, Warehouse
from .forms import SupplierForm, CustomerForm, ProductForm, WarehouseForm

# Supplier Crud
class SupplierView(TemplateView):
    template_name = "master_data/supplier.html"

    def get_context_data(self, **kwargs):
        data = Supplier.objects.all()
        context = {
            "page_title": "Master Data Supplier",
            "data": data
        }
        return context


class SupplierFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = Supplier.objects.get(SupplierPk=kwargs['pk'])
            data = model.__dict__
            self.forms = SupplierForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Supplier',
                'forms': self.forms
            }
        else:
            self.forms = SupplierForm()
            self.context = {
                'page_title': 'Create New Supplier',
                'forms': self.forms
            }
        return render(self.request, 'master_data/supplier_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = Supplier.objects.get(SupplierPk=kwargs['pk'])
            self.forms = SupplierForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('supplier'))
            else:
                self.context = {
                    'page_title': 'Edit Supplier',
                'forms': self.forms
                }
                return render(self.request, 'master_data/supplier_form.html', self.context)
        else:
            self.forms = SupplierForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('supplier'))
            else:
                self.context = {
                    'page_title': 'Create New Supplier',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/supplier_form.html', self.context)


class DeleteSupplierView(DeleteView):
    # login_url = "/account/login/"
    model = Supplier
    template_name = 'master_data/supplier_confirm_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('supplier')


# Customer Crud
class CustomerView(TemplateView):
    template_name = "master_data/customer.html"

    def get_context_data(self, **kwargs):
        data = Customer.objects.all()
        context = {
            "page_title": "Master Data Customer",
            "data": data
        }
        return context


class CustomerFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = Customer.objects.get(CustomerPk=kwargs['pk'])
            data = model.__dict__
            self.forms = CustomerForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Customer',
                'forms': self.forms
            }
        else:
            self.forms = CustomerForm()
            self.context = {
                'page_title': 'Create New Customer',
                'forms': self.forms
            }
        return render(self.request, 'master_data/customer_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = Customer.objects.get(CustomerPk=kwargs['pk'])
            self.forms = CustomerForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('customer'))
            else:
                self.context = {
                    'page_title': 'Edit Customer',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/customer_form.html', self.context)
        else:
            self.forms = CustomerForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('customer'))
            else:
                self.context = {
                    'page_title': 'Create New Customer',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/customer_form.html', self.context)


class DeleteCustomerView(DeleteView):
    # login_url = "/account/login/"
    model = Customer
    template_name = 'master_data/customer_confirm_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('customer')


# Product Crud
class ProductView(TemplateView):
    template_name = "master_data/product.html"

    def get_context_data(self, **kwargs):
        data = Product.objects.all()
        context = {
            "page_title": "Master Data Product",
            "data": data
        }
        return context


class ProductFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = Product.objects.get(ProductPk=kwargs['pk'])
            data = model.__dict__
            self.forms = ProductForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Product',
                'forms': self.forms
            }
        else:
            self.forms = ProductForm()
            self.context = {
                'page_title': 'Create New Product',
                'forms': self.forms
            }
        return render(self.request, 'master_data/product_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = Product.objects.get(ProductPk=kwargs['pk'])
            self.forms = ProductForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('product'))
            else:
                self.context = {
                    'page_title': 'Edit Product',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/product_form.html', self.context)
        else:
            self.forms = ProductForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('product'))
            else:
                self.context = {
                    'page_title': 'Create New Product',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/product_form.html', self.context)


class DeleteProductView(DeleteView):
    # login_url = "/account/login/"
    model = Product
    template_name = 'master_data/product_confirm_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('product')


# Warehouse Crud
class WarehouseView(TemplateView):
    template_name = "master_data/warehouse.html"

    def get_context_data(self, **kwargs):
        data = Warehouse.objects.all()
        context = {
            "page_title": "Master Data Warehouse",
            "data": data
        }
        return context


class WarehouseFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = Warehouse.objects.get(WhsPk=kwargs['pk'])
            data = model.__dict__
            self.forms = WarehouseForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Warehouse',
                'forms': self.forms
            }
        else:
            self.forms = WarehouseForm()
            self.context = {
                'page_title': 'Create New Warehouse',
                'forms': self.forms
            }
        return render(self.request, 'master_data/warehouse_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = Warehouse.objects.get(WhsPk=kwargs['pk'])
            self.forms = WarehouseForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('warehouse'))
            else:
                self.context = {
                    'page_title': 'Edit Warehouse',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/warehouse_form.html', self.context)
        else:
            self.forms = WarehouseForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('warehouse'))
            else:
                self.context = {
                    'page_title': 'Create New Warehouse',
                    'forms': self.forms
                }
                return render(self.request, 'master_data/warehouse_form.html', self.context)


class DeleteWarehouseView(DeleteView):
    # login_url = "/account/login/"
    model = Warehouse
    template_name = 'master_data/warehouse_confirm_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('warehouse')