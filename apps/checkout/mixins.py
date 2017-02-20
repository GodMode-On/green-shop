
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

from oscar.apps.checkout import mixins as oscar_mixins
from oscar.core.compat import get_user_model


User = get_user_model()


class OrderPlacementMixin(oscar_mixins.OrderPlacementMixin):
    def handle_successful_order(self, order):
        response = super(
            OrderPlacementMixin, self).handle_successful_order(order)
        self.send_notification_message(order)
        return response

    def send_notification_message(self, order):
        email_message = unicode(_("New order:{}".format(order.pk)))

        send_mail(
            u"New order",
            email_message,
            'info@shop.com',
            [user.email for user in User.objects.filter(is_staff=True)],
        )
