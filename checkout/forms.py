from django import forms
from .models import Order


class orderform(forms.Modelform):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'town', 'postcode',
                  'county', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Placeholder for form and field focus
        """
        super().__init__(*args **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number' : 'Phone Number',
            'Stree_address' : 'Street Address',
            'town' : 'Town',
            'county' : 'County',
            'postcode' : 'Postcode',
            'country' :  'Country',
        }

        self.felds['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholder[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field.widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        }