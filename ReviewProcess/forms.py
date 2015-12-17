from django import forms


class ContactForm(forms.Form):
    phone = forms.CharField(max_length=100)
    emailid = forms.CharField(max_length=100)
