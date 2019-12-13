from django import forms
from .models import *
from captcha.fields import CaptchaField


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(required=False, max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e. hello@world.com'}), error_messages={'invalid': 'Please enter an email in this format: hello@world.com'})
    #captcha = CaptchaField()

    class Meta:
        # This needs to be here to make the form work as an object.
        model = Subscription
        fields = ['email']
