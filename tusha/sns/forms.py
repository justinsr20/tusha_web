from django import forms


class AddNumberForm(forms.Form):
    contact_number = forms.CharField(label='Add contact number')


class RemoveNumberForm(forms.Form):
    contact_number = forms.CharField(label='Remove contact number')


class ContactForm(forms.Form):
    contact_content = forms.CharField(widget=forms.Textarea,
                                      label='Notify contacts')
