from oscar.apps.dashboard.catalogue import views as oscar_views

from apps.catalogue.models import Product, ProductCategory


class ProductListView(oscar_views.ProductListView):
    def get_queryset(self):
        """
        Build the queryset for this list
        """
        queryset = Product.objects.base_queryset()
        queryset = self.filter_queryset(queryset)
        queryset = self.apply_search(queryset)
        return queryset


class ProductCreateUpdateView(oscar_views.ProductCreateUpdateView):
    def forms_valid(self, form, formsets):
        response = super(
            ProductCreateUpdateView, self).forms_valid(form, formsets)

        if self.object.is_child:
            self.object.product_class = self.object.parent.product_class
            for cat in self.object.parent.categories.all():
                ProductCategory.objects.get_or_create(
                    product=self.object, category=cat)

        self.object.save()
        return response
