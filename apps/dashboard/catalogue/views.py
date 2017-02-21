from oscar.apps.dashboard.catalogue import views as oscar_views

from apps.catalogue.models import Product


class ProductListView(oscar_views.ProductListView):
    def get_queryset(self):
        """
        Build the queryset for this list
        """
        queryset = Product.objects.base_queryset()
        queryset = self.filter_queryset(queryset)
        queryset = self.apply_search(queryset)
        return queryset
