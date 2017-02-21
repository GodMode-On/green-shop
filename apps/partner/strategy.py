from decimal import Decimal as D

from apps.partner.prices import FixedPrice

from oscar.core.loading import get_class

Unavailable = get_class('partner.availability', 'Unavailable')
UnavailablePrice = get_class('partner.prices', 'Unavailable')
# FixedPrice = get_class('partner.prices', 'FixedPrice')
UseFirstStockRecord = get_class('partner.strategy', 'UseFirstStockRecord')
StockRequired = get_class('partner.strategy', 'StockRequired')
Structured = get_class('partner.strategy', 'Structured')


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        return Ukraine(request)


class NoTax(object):
    """
    Pricing policy mixin for use with the ``Structured`` base strategy.
    This mixin specifies zero tax and uses the ``price_excl_tax`` from the
    stockrecord.
    """

    def pricing_policy(self, product, stockrecord):
        # Check stockrecord has the appropriate data
        if not stockrecord or stockrecord.price_excl_tax is None:
            return UnavailablePrice()
        return FixedPrice(
            currency=stockrecord.price_currency,
            excl_tax=stockrecord.price_excl_tax,
            tax=D('0.00'),
            sale_price=stockrecord.sale_price)

    def parent_pricing_policy(self, product, children_stock):
        stockrecords = [x[1] for x in children_stock if x[1] is not None]
        if not stockrecords:
            return UnavailablePrice()
        # We take price from first record
        stockrecord = stockrecords[0]
        return FixedPrice(
            currency=stockrecord.price_currency,
            excl_tax=stockrecord.price_excl_tax,
            tax=D('0.00'),
            sale_price=stockrecord.sale_price)


class Ukraine(UseFirstStockRecord, StockRequired, NoTax, Structured):
    """
    Default stock/price strategy that uses the first found stockrecord for a
    product, ensures that stock is available (unless the product class
    indicates that we don't need to track stock) and charges zero tax.
    """
