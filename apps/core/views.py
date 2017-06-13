import logging
from django.shortcuts import render

log = logging.getLogger(__name__)


def test_view(request):
    log.info('view visited')
    return render(request, 'test.html')
