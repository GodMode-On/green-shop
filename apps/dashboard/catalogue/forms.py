from django import forms
from django.forms.models import inlineformset_factory

from oscar.core.loading import get_model

from oscar.apps.dashboard.catalogue.forms import (
    StockRecordForm as OscarStockrecordForm,
    ProductForm as OscarProductForm)


StockRecord = get_model('partner', 'StockRecord')
Partner = get_model('partner', 'Partner')
Product = get_model('catalogue', 'Product')


class StockRecordForm(OscarStockrecordForm):
    def __init__(self, product_class, user, *args, **kwargs):
        # The user kwarg is not used by stock StockRecordForm. We pass it
        # anyway in case one wishes to customise the partner queryset
        self.user = user
        super(OscarStockrecordForm, self).__init__(*args, **kwargs)

        self.fields['price_excl_tax'].required = True
        self.fields['partner_sku'].initial = "UAH"
        self.add_default_partner()

    def add_default_partner(self):
        default_partner, created = Partner.objects.get_or_create(
            name="Default Partner")
        self.fields['partner'].initial = default_partner
        self.fields['partner_sku'].initial = "00000"

    class Meta:
        model = StockRecord
        fields = [
            'partner', 'partner_sku',
            'price_currency', 'price_excl_tax',
            'num_in_stock',
        ]
        widgets = {
            'partner': forms.HiddenInput(),
            'partner_sku': forms.HiddenInput(),
            'price_currency': forms.HiddenInput(),
        }


BaseStockRecordFormSet = inlineformset_factory(
    Product, StockRecord, form=StockRecordForm, extra=1)


class StockRecordFormSet(BaseStockRecordFormSet):
    def __init__(self, product_class, user, *args, **kwargs):
        self.user = user
        self.product_class = product_class

        if not user.is_staff and \
           'instance' in kwargs and \
           'queryset' not in kwargs:
            kwargs.update({
                'queryset': StockRecord.objects.filter(
                    product=kwargs['instance'],
                    partner__in=user.partners.all())
            })

        super(BaseStockRecordFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        kwargs['product_class'] = self.product_class
        kwargs['user'] = self.user
        return super(StockRecordFormSet, self)._construct_form(
            i, **kwargs)


class ProductForm(OscarProductForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['upc'].initial = self.generate_upc()

    def generate_upc(self):
        return int(Product.objects.order_by('-pk')[0].pk) + 1

    class Meta:
        model = Product
        fields = [
            'title', 'upc', 'description', 'is_discountable', 'structure',
            'presentation']
        widgets = {
            'structure': forms.HiddenInput(),
            'is_discountable': forms.HiddenInput(),
            'upc': forms.HiddenInput(),
        }
