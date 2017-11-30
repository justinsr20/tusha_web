from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^all_contacts', views.all_contacts, name='all_contacts'),
    url(r'^add_contact', views.add_contact, name='add_contact'),
    url(r'^remove_contact', views.remove_contact, name='remove_contact'),
    url(r'^notify_contacts', views.notify_contacts, name='notify_contacts'),
]
