from django import forms

from authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['info', 'image_url']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
        }
        help_texts = {
            'passcode': "Your passcode must be a combination of 6 digits"
        }

        widgets = {
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }


class AuthorCreateForm(AuthorBaseForm):
    pass

class AuthorEditForm(AuthorBaseForm):
    pass

class AuthorDeleteForm(AuthorBaseForm):
    pass
