from django.http import HttpResponsePermanentRedirect


from oscar.apps.catalogue import views as oscar_views


class ProductDetailView(oscar_views.ProductDetailView):
    # Whether to redirect parent products to their 1st childs's URL
    redirect_parent = True

    def get(self, request, **kwargs):
        """
        Ensures that the correct URL is used before rendering a response
        """
        self.object = product = self.get_object()

        redirect = self.redirect_if_necessary(request.path, product)
        if redirect is not None:
            return redirect

        response = super(
            oscar_views.ProductDetailView, self).get(request, **kwargs)
        self.send_signal(request, response, product)
        return response

    def redirect_if_necessary(self, current_path, product):
        if self.redirect_parent and product.is_parent:
            return HttpResponsePermanentRedirect(
                product.children.all()[0].get_absolute_url())
