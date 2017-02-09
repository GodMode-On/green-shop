from oscar.core.loading import get_class

OscarFixedPrice = get_class('partner.prices', 'FixedPrice')


class FixedPrice(OscarFixedPrice):
    sale_price = None

    def __init__(self, currency, excl_tax, tax=None, sale_price=None):
        self.currency = currency
        self.excl_tax = excl_tax
        self.tax = tax
        self.sale_price = sale_price

    @property
    def sale_discount(self):
        if self.sale_price:
            return self.excl_tax - self.sale_price
        return None

    @property
    def sale_discount_percent(self):
        if self.sale_price:
            return round((
                self.excl_tax - self.sale_price) / self.excl_tax * 100)
        return None
