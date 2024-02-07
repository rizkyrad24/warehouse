from django.urls import path
from .views import *

urlpatterns = [
    # Supplier url
    path("supplier", SupplierView.as_view(), name="supplier"),
    path("supplier/create", SupplierFormView.as_view(), name="create-supplier"),
    path("supplier/edit/<int:pk>", SupplierFormView.as_view(), name="edit-supplier"),
    path("supplier/delete/<int:pk>", DeleteSupplierView.as_view(), name="delete-supplier"),

    # Customer url
    path("customer", CustomerView.as_view(), name="customer"),
    path("customer/create", CustomerFormView.as_view(), name="create-customer"),
    path("customer/edit/<int:pk>", CustomerFormView.as_view(), name="edit-customer"),
    path("customer/delete/<int:pk>", DeleteCustomerView.as_view(), name="delete-customer"),

    # Product url
    path("product", ProductView.as_view(), name="product"),
    path("product/create", ProductFormView.as_view(), name="create-product"),
    path("product/edit/<int:pk>", ProductFormView.as_view(), name="edit-product"),
    path("product/delete/<int:pk>", DeleteProductView.as_view(), name="delete-product"),

    # Warehouse url
    path("warehouse", WarehouseView.as_view(), name="warehouse"),
    path("warehouse/create", WarehouseFormView.as_view(), name="create-warehouse"),
    path("warehouse/edit/<int:pk>", WarehouseFormView.as_view(), name="edit-warehouse"),
    path("warehouse/delete/<int:pk>", DeleteWarehouseView.as_view(), name="delete-warehouse"),

]