import logging

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from apps.core.forms import PersonForm
from apps.core.models import Person

log = logging.getLogger(__name__)


class PersonListView(ListView):
    model = Person
    template_name = 'list.html'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'form.html'
    success_url = reverse_lazy('list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'form.html'
    success_url = reverse_lazy('list')


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('list')
    template_name = 'confirm_delete.html'
