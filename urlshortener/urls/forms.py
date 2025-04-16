from django.forms import ModelForm

from .models import URL


class URLForm(ModelForm):
    """
    A custom URL form.
    """
    class Meta:
        model = URL
        fields = ['url']
