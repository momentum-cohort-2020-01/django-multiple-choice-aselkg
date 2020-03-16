from django import forms

from .models import Snippet, Language

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('title', 'code', 'languages')


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('name',)