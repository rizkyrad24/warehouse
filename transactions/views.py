from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, View, RedirectView, DeleteView
from .models import PenerimaanBarangHeader, PenerimaanBarangDetail, PengeluaranBarangHeader, PengeluaranBarangDetail
from .forms import PenerimaanBarangHeaderForm, PenerimaanBarangDetailForm, PengeluaranBarangHeaderForm, PengeluaranBarangDetailForm

# PenerimaanBarangHeader Crud
class PenerimaanBarangHeaderView(TemplateView):
    template_name = "transactions/PenerimaanBarangHeader.html"

    def get_context_data(self, **kwargs):
        data = PenerimaanBarangHeader.objects.all()
        context = {
            "page_title": "Data Penerimaan",
            "data": data
        }
        return context


class PenerimaanBarangHeaderFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = PenerimaanBarangHeader.objects.get(TrxInPk=kwargs['pk'])
            data = model.__dict__
            self.forms = PenerimaanBarangHeaderForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Penerimaan Barang Header',
                'forms': self.forms
            }
        else:
            self.forms = PenerimaanBarangHeaderForm()
            self.context = {
                'page_title': 'Create New Penerimaan Barang Header',
                'forms': self.forms
            }
        return render(self.request, 'transactions/PenerimaanBarangHeader_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = PenerimaanBarangHeader.objects.get(TrxInPk=kwargs['pk'])
            self.forms = PenerimaanBarangHeaderForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('penerimaan-header'))
            else:
                self.context = {
                    'page_title': 'Edit Penerimaan Barang Header',
                'forms': self.forms
                }
                return render(self.request, 'transactions/PenerimaanBarangHeader_form.html', self.context)
        else:
            self.forms = PenerimaanBarangHeaderForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('penerimaan-header'))
            else:
                self.context = {
                    'page_title': 'Create New Penerimaan Barang Header',
                    'forms': self.forms
                }
                return render(self.request, 'transactions/PenerimaanBarangHeader_form.html', self.context)


class DeletePenerimaanBarangHeaderView(DeleteView):
    # login_url = "/account/login/"
    model = PenerimaanBarangHeader
    template_name = 'transactions/PenerimaanBarangHeader_confirm_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('penerimaan-header')


# PengeluaranBarangHeader Crud
class PengeluaranBarangHeaderView(TemplateView):
    template_name = "transactions/PengeluaranBarangHeader.html"

    def get_context_data(self, **kwargs):
        data = PengeluaranBarangHeader.objects.all()
        context = {
            "page_title": "Data Pengeluaran",
            "data": data
        }
        return context


class PengeluaranBarangHeaderFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = PengeluaranBarangHeader.objects.get(TrxOutPk=kwargs['pk'])
            data = model.__dict__
            self.forms = PengeluaranBarangHeaderForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Pengeluaran Barang Header',
                'forms': self.forms
            }
        else:
            self.forms = PengeluaranBarangHeaderForm()
            self.context = {
                'page_title': 'Create New Pengeluaran Barang Header',
                'forms': self.forms
            }
        return render(self.request, 'transactions/PengeluaranBarangHeader_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = PengeluaranBarangHeader.objects.get(TrxOutPk=kwargs['pk'])
            self.forms = PengeluaranBarangHeaderForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('pengeluaran-header'))
            else:
                self.context = {
                    'page_title': 'Edit Pengeluaran Barang Header',
                'forms': self.forms
                }
                return render(self.request, 'transactions/PengeluaranBarangHeader_form.html', self.context)
        else:
            self.forms = PengeluaranBarangHeaderForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('pengeluaran-header'))
            else:
                self.context = {
                    'page_title': 'Create New Pengeluaran Barang Header',
                    'forms': self.forms
                }
                return render(self.request, 'transactions/PengeluaranBarangHeader_form.html', self.context)


class DeletePengeluaranBarangHeaderView(DeleteView):
    # login_url = "/account/login/"
    model = PengeluaranBarangHeader
    template_name = 'transactions/PengeluaranBarangHeader_confirm_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('pengeluaran-header')


# PenerimaanBarangDetail Crud
class PenerimaanBarangDetailView(TemplateView):
    template_name = "transactions/PenerimaanBarangDetail.html"

    def get_context_data(self, **kwargs):
        data = PenerimaanBarangHeader.objects.get(TrxInPk=kwargs['pk'])
        # data = PenerimaanBarangDetail.objects.filter(TrxOutIDF=kwargs['trans_id'])
        context = {
            "page_title": "Data Penerimaan Produk",
            "data": data
        }
        return context


class PenerimaanBarangDetailFormView(View):

    def get(self, request, **kwargs):
        if kwargs.__contains__('pk'):
            model = PenerimaanBarangDetail.objects.get(TrxInDPK=kwargs['pk'])
            data = model.__dict__
            self.forms = PenerimaanBarangDetailForm(initial=data, instance=model)
            self.context = {
                'page_title': 'Edit Penerimaan Barang Detail',
                'forms': self.forms
            }
        else:
            trans = PenerimaanBarangHeader.objects.get(TrxInPk=kwargs['trans_id'])
            data = {'TrxInIDF': trans}
            self.forms = PenerimaanBarangDetailForm(initial=data)
            self.context = {
                'page_title': 'Tambahkan Detai Barang Yang Diterima',
                'forms': self.forms
            }
        return render(self.request, 'transactions/PenerimaanBarangDetail_form.html', self.context)
    
    def post(self, request, *args, **kwargs):
        if kwargs.__contains__('pk'):
            model = PenerimaanBarangDetail.objects.get(TrxInDPK=kwargs['pk'])
            self.forms = PenerimaanBarangDetailForm(request.POST, instance=model)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('penerimaan-detail', kwargs={'pk': model.TrxInIDF.TrxInPk}))
            else:
                self.context = {
                    'page_title': 'Edit Penerimaan Barang Detail',
                'forms': self.forms
                }
                return render(self.request, 'transactions/PenerimaanBarangDetail_form.html', self.context)
        else:
            trans = PenerimaanBarangHeader.objects.get(TrxInPk=kwargs['trans_id'])
            self.forms = PenerimaanBarangDetailForm(request.POST)
            if self.forms.is_valid():
                self.forms.save()
                return redirect(reverse('penerimaan-detail', kwargs={'pk': trans.TrxInPk}))
            else:
                self.context = {
                    'page_title': 'Create New Penerimaan Barang Detail',
                    'forms': self.forms
                }
                return render(self.request, 'transactions/PenerimaanBarangDetail_form.html', self.context)


class DeletePenerimaanBarangDetailView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        record = PenerimaanBarangDetail.objects.get(TrxInDPK=kwargs['pk'])
        url = reverse('penerimaan-detail', kwargs={'pk': record.TrxInIDF.TrxInPk})
        record.delete()
        return url