from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Message',
        }
    ))

    class Meta:
        model = Message
        fields = ['message']