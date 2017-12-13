# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView
)

from sns.lib.sns import remove_subscription, add_subscription, notify_subscriptions
from .forms import AddNumberForm, RemoveNumberForm, ContactForm, CustomAuthenticationForm
from .models import CustomerContacts


class Login(LoginView):
    form_class = CustomAuthenticationForm


@login_required
def index(request):
    return render(request, 'index.html', {})


@login_required
def all_contacts(request):
    c = CustomerContacts.objects.all()
    return render(request, 'all_contacts.html', {'customers': c})


@login_required
def add_contact(request):
    if request.method == 'POST':
        form = AddNumberForm(request.POST)
        if form.is_valid():
            new_customer = CustomerContacts(mobile_contact_number=form.cleaned_data['contact_number'],
                                            first_name=form.cleaned_data['contact_first_name'],
                                            last_name=form.cleaned_data['contact_last_name'])
            add_subscription(form.cleaned_data['contact_number'])
            new_customer.save()
            return redirect(all_contacts)
    else:
        form = AddNumberForm()

    return render(request, 'add_contact.html', {'form': form})


@login_required
def remove_contact(request):
    if request.method == 'POST':
        form = RemoveNumberForm(request.POST)
        if form.is_valid():
            c = CustomerContacts.objects.get(mobile_contact_number=form.cleaned_data['contact_number'])
            remove_subscription(form.cleaned_data['contact_number'])
            c.delete()
            return redirect(all_contacts)
    else:
        form = RemoveNumberForm()

    return render(request, 'remove_contact.html', {'form': form})


@login_required
def notify_contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            notify_subscriptions(form.cleaned_data['contact_content'])
            return redirect(all_contacts)
    else:
        form = ContactForm()

    return render(request, 'notify_contacts.html', {'form': form})
