from django import forms
from ReviewProcess.models import UpdateUserInfo

class ContactForm(forms.Form):
    phone = forms.CharField(max_length=100)
    emailid = forms.CharField(max_length=100)

class UpdateProfileForm(forms.ModelForm):
    """
    """
    class Meta:
        model=UpdateUserInfo
        exclude=()