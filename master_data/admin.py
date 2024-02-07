from django.contrib import admin
from .models import Supplier, Customer, Product, Warehouse

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('SupplierPk', 'SupplierName',)
    search_fields = ('SupplierName',)

admin.site.register(Supplier, SupplierAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('CustomerPk', 'CustomerName',)
    search_fields = ('CustomerName',)

admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductPk', 'ProductName',)
    search_fields = ('ProductName',)

admin.site.register(Product, ProductAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('WhsPk', 'WhsName',)
    search_fields = ('WhsName',)

admin.site.register(Warehouse, WarehouseAdmin)
