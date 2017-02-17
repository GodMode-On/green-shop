from oscar.core.loading import get_model
from oscar.apps.address import forms as oscar_forms


UserAddress = get_model('address', 'useraddress')
Country = get_model('address', 'Country')


class UserAddressForm(oscar_forms.UserAddressForm):
    class Meta:
        model = UserAddress
        fields = [
            'first_name', 'last_name',
            'line1', 'line2', 'line4',
            'postcode', 'country',
            'phone_number', 'notes',
        ]

    def __init__(self, user, *args, **kwargs):
        super(UserAddressForm, self).__init__(user, *args, **kwargs)
        self.fields['country'].initial = Country.objects.get(
            printable_name="Ukraine")
        self.fields['phone_number'].required = True
