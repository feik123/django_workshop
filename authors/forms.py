from django import forms

from authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        help_texts = {
            "passcode": "Your passcode must be a combination of 6 digits"dadas
        }


class AuthorCreateForm(AuthorBaseForm):
    pass


class AuthorEditForm(AuthorBaseForm):
    pass


class AuthorDeleteForm(AuthorBaseForm):
    pass
