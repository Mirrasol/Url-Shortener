from django.forms import ModelForm

from .models import URL
# from django import forms


# class URLForm(forms.Form):
#     url = forms.URLField(label='URL')


class URLForm(ModelForm):
    """
    A custom URL form.
    """
    class Meta:
        model = URL
        fields = ['url']
