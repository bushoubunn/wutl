from django import forms

class TranslateForm(forms.Form):

    content=forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'input-text'}))