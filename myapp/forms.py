from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms
from .models import Snippet


def splitting(str):
    return str.split(' ')

class ContactForm(forms.Form):
    sentence = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'It\'s a beautiful day outside. Birds are singing, flowers are blooming.'}))
#    sentence = forms.CharField()

#    def __init__(self,*args,**kwargs):
#        super().__init__(*args,**kwargs)
#
#       self.helper = FormHelper
#       self.helper.form_method = 'post'

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('sentence',)

#un commentaire