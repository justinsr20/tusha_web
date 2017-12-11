from django import forms
from sns.lib.validators import all_numbers_validator, min_length_validator, not_start_with_zero_validator, \
    word_only_letters

number_validators = [all_numbers_validator, min_length_validator, not_start_with_zero_validator]


class AddNumberForm(forms.Form):
    contact_number = forms.CharField(label='Add contact number',
                                     validators=number_validators,
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Enter number'}))
    contact_first_name = forms.CharField(label='First Name',
                                         validators=[word_only_letters],
                                         widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Enter first name'}))
    contact_last_name = forms.CharField(label='Last Name',
                                        validators=[word_only_letters],
                                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Enter first name'}))


class RemoveNumberForm(forms.Form):
    contact_number = forms.CharField(label='Remove contact number',
                                     validators=number_validators,
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Enter number'}))


class ContactForm(forms.Form):
    contact_content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                   'placeholder': 'Enter message here'}),
                                      label='Notify contacts')
