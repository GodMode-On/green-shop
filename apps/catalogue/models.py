from django.db import models
from django.utils.translation import ugettext_lazy as _

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    presentation = models.CharField(
        _("Presentation"), max_length=64, blank=True, null=True)

    @property
    def get_title_for_dropdown(self):
        if self.presentation:
            return self.presentation
        elif self.title:
            return self.title
        else:
            return _("Product {}".format(self.pk))

    @property
    def get_description(self):
        if self.is_child:
            return self.parent.description
        return self.description

    def _clean_child(self):
        """
        Validates a child product
        """
        if not self.parent_id:
            raise ValidationError(_("A child product needs a parent."))
        if self.parent_id and not self.parent.is_parent:
            raise ValidationError(
                _("You can only assign child products to parent products."))
        # Note that we only forbid options on product level
        if self.pk and self.product_options.exists():
            raise ValidationError(
                _("A child product can't have options."))

from oscar.apps.catalogue.models import *  # noqa
