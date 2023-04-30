from django import forms

class URLForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter URL of file to download'
    }))
