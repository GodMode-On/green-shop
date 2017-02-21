from django.db import models

from oscar.apps.catalogue import managers as oscar_managers


class ProductQuerySet(oscar_managers.ProductQuerySet):
    def browsable(self):
        """
        Excludes non-canonical products.
        """
        return self.filter(structure__in=['child', 'standalone'])


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def browsable(self):
        return self.get_queryset().browsable()

    def base_queryset(self):
        return self.get_queryset().base_queryset()


class BrowsableProductManager(ProductManager):
    def get_queryset(self):
        return super(BrowsableProductManager, self).get_queryset().browsable()
