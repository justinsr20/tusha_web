from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(template_name='sns/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^all_contacts/$', views.all_contacts, name='all_contacts'),
    url(r'^add_contact/$', views.add_contact, name='add_contact'),
    url(r'^remove_contact/$', views.remove_contact, name='remove_contact'),
    url(r'^notify_contacts/$', views.notify_contacts, name='notify_contacts'),
]
