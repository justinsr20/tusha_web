from django import forms
from sns.lib.validators import all_numbers_validator, min_length_validator, not_start_with_zero_validator


class AddNumberForm(forms.Form):
    contact_number = forms.CharField(label='Add contact number',
                                     validators=[all_numbers_validator, min_length_validator,
                                                 not_start_with_zero_validator])


class RemoveNumberForm(forms.Form):
    contact_number = forms.CharField(label='Remove contact number')


class ContactForm(forms.Form):
    contact_content = forms.CharField(widget=forms.Textarea,
                                      label='Notify contacts')
