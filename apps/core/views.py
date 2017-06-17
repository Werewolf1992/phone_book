import logging
from django.shortcuts import render
from apps.core.models import Person
from config.settings import BASE_DIR

log = logging.getLogger(__name__)


def test_view(request):
    contacts = Person.objects.all().order_by('name')
    log.info('view visited')
    return render(request, 'contacts_list.html', {'contacts': contacts, 'BASE_DIR': BASE_DIR})
