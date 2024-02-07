from collections.abc import Iterable
from django.db import models
from master_data.models import Supplier, Customer, Product, Warehouse
import uuid
import datetime

# Create your models here.
# class StockProduct(models.Model):
#     StockPk = models.AutoField(primary_key=True)
#     WhsIdf = models.ForeignKey(Warehouse, on_delete= models.CASCADE, related_name="Stock")
#     ProductIdf = models.ForeignKey(Product, on_delete= models.CASCADE, related_name="Stock")
#     UniqueStr = models.CharField(max_length=255, blank=True)
#     QtyDus = models.IntegerField(default=0)
#     QtyPcs = models.IntegerField(default=0)
#     Update_At = models.DateTimeField(auto_now=True)
#     Created_At = models.DateTimeField(auto_now_add=True)


class PenerimaanBarangHeader(models.Model):
    TrxInPk = models.AutoField(primary_key=True)
    TrxInNo = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    WhsIdf = models.ForeignKey(Warehouse, on_delete= models.CASCADE, related_name="Penerimaan_header")
    TrxInDate = models.DateField(default=datetime.date.today)
    TrxInSuppIdf = models.ForeignKey(Supplier, on_delete= models.CASCADE, related_name="Penerimaan_header")
    TrxInNotes = models.TextField(null=True, blank=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.TrxInNo}'


class PenerimaanBarangDetail(models.Model):
    TrxInDPK = models.AutoField(primary_key=True)
    TrxInIDF = models.ForeignKey(PenerimaanBarangHeader, on_delete= models.CASCADE, related_name="Penerimaan_detail")
    TrxInDProductIdf = models.ForeignKey(Product, on_delete= models.CASCADE, related_name="Penerimaan_detail")
    TrxInDQtyDus = models.IntegerField(default=0)
    TrxInDQtyPcs = models.IntegerField(blank=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        self.TrxInDQtyPcs = self.TrxInDQtyDus * self.TrxInDProductIdf.QtyPcsPerDus
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.TrxInIDF}'


class PengeluaranBarangHeader(models.Model):
    TrxOutPk = models.AutoField(primary_key=True)
    TrxOutNo = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    WhsIdf = models.ForeignKey(Warehouse, on_delete= models.CASCADE, related_name="Pengeluaran_header")
    TrxOutDate = models.DateField(default=datetime.date.today)
    TrxOutSuppIdf = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name="Pengeluaran_header")
    TrxOutNotes = models.TextField(null=True, blank=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.TrxOutNo}'


class PengeluaranBarangDetail(models.Model):
    TrxOutDPK = models.AutoField(primary_key=True)
    TrxOutIDF = models.ForeignKey(PengeluaranBarangHeader, on_delete= models.CASCADE, related_name="Pengeluaran_detail")
    TrxOutDProductIdf = models.ForeignKey(Product, on_delete= models.CASCADE, related_name="Pengeluaran_detail")
    TrxOutDQtyDus = models.IntegerField(default=0)
    TrxOutDQtyPcs = models.IntegerField(blank=True)
    Update_At = models.DateTimeField(auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        self.TrxOutDQtyPcs = self.TrxOutDQtyDus * self.TrxOutDProductIdf.QtyPcsPerDus
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.TrxOutIDF}'