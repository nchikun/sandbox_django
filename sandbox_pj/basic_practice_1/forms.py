from django import forms
from .models import Posting


class PostingForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 4})
        }
