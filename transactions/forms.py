from django import forms
from .models import *

class PenerimaanBarangHeaderForm(forms.ModelForm):
    class Meta:
        model = PenerimaanBarangHeader
        fields = ['WhsIdf', 'TrxInDate', 'TrxInSuppIdf', 'TrxInNotes',]
        widgets = {
            'WhsIdf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'TrxInDate': forms.DateInput(attrs={
                'class': 'form-select'
            }),
            'TrxInSuppIdf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'TrxInNotes': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class PenerimaanBarangDetailForm(forms.ModelForm):
    class Meta:
        model = PenerimaanBarangDetail
        fields = ['TrxInIDF' ,'TrxInDProductIdf', 'TrxInDQtyDus']
        widgets = {
            'TrxInIDF': forms.Select(attrs={
                'class': 'd-none'
            }),
            'TrxInDProductIdf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'TrxInDQtyDus': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class PengeluaranBarangHeaderForm(forms.ModelForm):
    class Meta:
        model = PengeluaranBarangHeader
        fields = ['WhsIdf', 'TrxOutDate', 'TrxOutSuppIdf', 'TrxOutNotes',]
        widgets = {
            'WhsIdf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'TrxOutDate': forms.DateInput(attrs={
                'class': 'form-select'
            }),
            'TrxOutSuppIdf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'TrxOutNotes': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class PengeluaranBarangDetailForm(forms.ModelForm):
    class Meta:
        model = PengeluaranBarangDetail
        fields = ['TrxOutIDF', 'TrxOutDProductIdf', 'TrxOutDQtyDus']
        widgets = {
            'TrxOutIDF': forms.Select(attrs={
                'class': 'd-none'
            }),
            'TrxOutDProductIdf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'TrxOutDQtyDus': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }