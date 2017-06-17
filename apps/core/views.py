import logging

from django.shortcuts import render, redirect, get_object_or_404

from apps.core.forms import PersonForm
from apps.core.models import Person

log = logging.getLogger(__name__)


def list_view(request):
    contacts = Person.objects.all().order_by('name')
    log.info('List  view visited')
    return render(request, 'list.html', {'contacts': contacts})


def add_view(request):
    log.info('Add view visited')
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PersonForm()
    return render(request, 'add.html', {'form': form})


def edit_view(request, person_id):
    log.info('Edit view visited')
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'edit.html', {'form': form})


def person_delete(request, person_id):
        query = Person.objects.get(id=person_id)
        query.delete()
        return redirect('list')
