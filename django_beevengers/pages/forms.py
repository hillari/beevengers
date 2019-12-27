from django import forms
from .models import *
from captcha.fields import CaptchaField

"""
    **This will later be used for a subscription section on the homepage.**
"""

"""class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. hello@world.com'}), error_messages={'invalid': 'Please enter an email in this format: hello@world.com'})
    #captcha = CaptchaField()

    class Meta:
        # This needs to be here to make the form work as an object.
        model = Subscription
        fields = ['email']
"""
