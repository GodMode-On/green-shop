from django import forms
from django.utils.translation import ugettext_lazy as _

from oscar.forms import widgets
from oscar.core.loading import get_model

from oscar.apps.basket.forms import AddToBasketForm as OscarAddToBAsketForm

Product = get_model('catalogue', 'product')


class AddToBasketForm(OscarAddToBAsketForm):
    def __init__(self, basket, product, *args, **kwargs):
        self.basket = basket
        self.parent_product = product

        super(OscarAddToBAsketForm, self).__init__(*args, **kwargs)

        # Dynamically build fields
        if not product.is_standalone:
            self._create_parent_product_fields(product)

    def _create_parent_product_fields(self, product):
        """
        Adds the fields for a "group"-type product (eg, a parent product with a
        list of children.
        Currently requires that a stock record exists for the children
        """
        choices = []
        disabled_values = []
        child_products = []
        if product.is_parent:
            child_products = product.children.all()
        elif product.is_child:
            child_products = product.parent.children.all()
        for child in child_products:
            summary = child.get_title_for_dropdown
            choices.append((child.get_absolute_url(), summary))
        self.fields['child_id'] = forms.ChoiceField(
            choices=tuple(choices), label=_("Size"),
            widget=widgets.AdvancedSelect(disabled_values=disabled_values))
        self.fields = self.fields.__class__(self.fields.items()[::-1])

    def clean_child_id(self):
        try:
            if self.parent_product.is_parent:
                child = self.parent_product.children.get(
                    id=self.cleaned_data['child_id'].split('_')[-1][:-1])
            elif self.parent_product.is_child:
                child = self.parent_product.parent.children.get(
                    id=self.cleaned_data['child_id'].split('_')[-1][:-1])
        except Product.DoesNotExist:
            raise forms.ValidationError(
                _("Please select a valid product"),
                code='invalid')

        # To avoid duplicate SQL queries, we cache a copy of the loaded child
        # product as we're going to need it later.
        self.child_product = child

        return self.cleaned_data['child_id']
