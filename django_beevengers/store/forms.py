from django import forms
from .models import *

STATE_CHOICES = [
             ('AK', 'Alaska'), ('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
             ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'),
             ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
             ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
             ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
             ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
             ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
             ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'),
             ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
             ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]


QUANTITY_CHOICES = [
    ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'),
    ('eight', '8'), ('nine', '9'), ('more than 10', '10+')
]


class ProductForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.RegexField(required=True, regex=r'^\+?1?\d{9,15}$', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. 1234567890'}),error_messages={'invalid': 'Please enter a phone numer in this format: 1234567890'})
    email = forms.EmailField(required=False, max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. hello@world.com'}), error_messages={'invalid': 'Please enter an email in this format: hello@world.com'})
    quantity = forms.CharField(required=True, max_length=200, widget=forms.Select(choices=QUANTITY_CHOICES, attrs={'class': 'form-control'}))
    address = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. 1234 Main St'}))
    address_2 = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. Apartment, studio, or floor'}))
    city = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(required=True, max_length=200, widget=forms.Select(choices=STATE_CHOICES, attrs={'class': 'form-control'}))
    zip_code = forms.RegexField(required=True, regex='^(^[0-9]{5}(?:-[0-9]{4})?$|^$)', help_text='Zip Code',
                                error_messages={'required': 'This value is required',
                                                'invalid': 'Please enter a zip code in this format: 12345'},
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. 12345'}))

    class Meta:
        # This needs to be here to make the form work as an object.
        model = OrderRequest
        fields = ['first_name']