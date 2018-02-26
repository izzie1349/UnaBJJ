# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    contact_name = form.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=False)
