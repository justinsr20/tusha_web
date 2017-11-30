# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from sns.lib.sns import remove_subscription, add_subscription, all_subscriptions, notify_subscriptions
from tusha.settings import AWS_TUSHA_PROMOTIONS_TOPIC_ARN
from .forms import AddNumberForm, RemoveNumberForm, ContactForm


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def all_contacts(request):
    topic = all_subscriptions(AWS_TUSHA_PROMOTIONS_TOPIC_ARN)
    return render(request, 'all_contacts.html', {'topic': topic['Subscriptions']})


def add_contact(request):
    if request.method == 'POST':
        form = AddNumberForm(request.POST)
        if form.is_valid():
            add_subscription(form.cleaned_data['contact_number'])
            return redirect(all_contacts)
    else:
        form = AddNumberForm()

    return render(request, 'add_contact.html', {'form': form})


def remove_contact(request):
    if request.method == 'POST':
        form = RemoveNumberForm(request.POST)
        if form.is_valid():
            remove_subscription(form.cleaned_data['contact_number'])
            return redirect(all_contacts)
    else:
        form = RemoveNumberForm()

    return render(request, 'remove_contact.html', {'form': form})


def notify_contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            notify_subscriptions(form.cleaned_data['contact_content'])
            return redirect(all_contacts)
    else:
        form = ContactForm()

    return render(request, 'notify_contacts.html', {'form': form})
