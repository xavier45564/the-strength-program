from email import message
from functools import WRAPPER_ASSIGNMENTS
from django import forms
from .models import *
from django.forms import ModelForm

class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Comments...', 'class':'contacts-icon contactss-message'}), )
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'dxCode', 'phone', 'agency']
        message = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group', 'name': 'name', 'placeholder': 'Your Name...'}),
            'agency': forms.TextInput(attrs={'class': 'form-group', 'name': 'agency', 'placeholder': 'Referring Agency'}),
            'email': forms.TextInput(attrs={'class': 'form-group', 'name': 'email', 'placeholder': 'Your Email...', 'rows': '5'}),
            'dxCode': forms.TextInput(attrs={'class': 'form-group', 'name': 'dxCode', 'placeholder': 'Therapist Dx Code...', 'rows': '5'}),
            'phone': forms.NumberInput(attrs={'class': 'form-group', 'name': 'phone', 'placeholder': 'Address Phone...', 'rows': '5'}),
            
        }


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'newsletter-form', 'name': 'email', 'placeholder': 'Email'}),
        }
