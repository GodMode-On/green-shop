from django.db import models
from django.utils.translation import ugettext_lazy as _

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    presentation = models.CharField(
        _("Presentation"), max_length=64, blank=True, null=True)

from oscar.apps.catalogue.models import *  # noqa
