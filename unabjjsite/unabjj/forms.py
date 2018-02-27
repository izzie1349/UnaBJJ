# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_phone = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)
