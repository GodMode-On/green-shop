# -*- coding: utf-8 -*-

from oscar.apps.checkout import forms
from oscar.core.loading import get_model


class ShippingAddressForm(forms.ShippingAddressForm):
    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['phone_number'].help_text = (
            "За цим номером ми зв'яжемось із Вам з приводу оплати і доставки")
        self.fields['country'].initial = 'UA'

    class Meta:
        model = get_model('order', 'shippingaddress')
        fields = [
            'first_name', 'last_name', 'phone_number',
            'line1', 'line2', 'postcode', 'country',
            'notes',
        ]
