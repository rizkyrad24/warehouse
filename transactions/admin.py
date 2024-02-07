from django.contrib import admin
from .models import *

# Register your models here.
class PenerimaanBarangHeaderAdmin(admin.ModelAdmin):
    list_display = ('TrxInNo', 'WhsIdf', 'TrxInSuppIdf', 'TrxInDate',)
    search_fields = ('WhsIdf',)
    list_filter = ('TrxInSuppIdf',)

admin.site.register(PenerimaanBarangHeader, PenerimaanBarangHeaderAdmin)


class PenerimaanBarangDetailAdmin(admin.ModelAdmin):
    list_display = ('TrxInIDF', 'TrxInDProductIdf', 'TrxInDQtyDus', 'TrxInDQtyPcs',)
    list_filter = ('TrxInIDF',)
    readonly_fields = ('TrxInDQtyPcs',)

admin.site.register(PenerimaanBarangDetail, PenerimaanBarangDetailAdmin)


class PengeluaranBarangHeaderAdmin(admin.ModelAdmin):
    list_display = ('TrxOutNo', 'WhsIdf', 'TrxOutSuppIdf', 'TrxOutDate',)
    search_fields = ('WhsIdf',)
    list_filter = ('TrxOutSuppIdf',)

admin.site.register(PengeluaranBarangHeader, PengeluaranBarangHeaderAdmin)


class PengeluaranBarangDetailAdmin(admin.ModelAdmin):
    list_display = ('TrxOutIDF', 'TrxOutDProductIdf', 'TrxOutDQtyDus', 'TrxOutDQtyPcs',)
    list_filter = ('TrxOutIDF',)
    readonly_fields = ('TrxOutDQtyPcs',)

admin.site.register(PengeluaranBarangDetail, PengeluaranBarangDetailAdmin)