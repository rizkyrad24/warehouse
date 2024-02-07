from django.urls import path
from .views import *

urlpatterns = [
    # Penerimaan url
    path("penerimaan", PenerimaanBarangHeaderView.as_view(), name="penerimaan-header"),
    path("penerimaan/create", PenerimaanBarangHeaderFormView.as_view(), name="create-penerimaan-header"),
    path("penerimaan/edit/<int:pk>", PenerimaanBarangHeaderFormView.as_view(), name="edit-penerimaan-header"),
    path("penerimaan/delete/<int:pk>", DeletePenerimaanBarangHeaderView.as_view(), name="delete-penerimaan-header"),

    # Penerimaan Detail Url
    path("penerimaan/detail/<int:pk>", PenerimaanBarangDetailView.as_view(), name="penerimaan-detail"),
    path("penerimaan/detail/create/<int:trans_id>", PenerimaanBarangDetailFormView.as_view(), name="create-penerimaan-detail"),
    path("penerimaan/detail/edit/<int:pk>", PenerimaanBarangDetailFormView.as_view(), name="edit-penerimaan-detail"),
    path("penerimaan/detail/delete/<int:pk>", DeletePenerimaanBarangDetailView.as_view(), name="delete-penerimaan-detail"),

    # Pengeluaran url
    path("pengeluaran", PengeluaranBarangHeaderView.as_view(), name="pengeluaran-header"),
    path("pengeluaran/create", PengeluaranBarangHeaderFormView.as_view(), name="create-pengeluaran-header"),
    path("pengeluaran/edit/<int:pk>", PengeluaranBarangHeaderFormView.as_view(), name="edit-pengeluaran-header"),
    path("pengeluaran/delete/<int:pk>", DeletePengeluaranBarangHeaderView.as_view(), name="delete-pengeluaran-header"),
]