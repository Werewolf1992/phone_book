from django.conf.urls import url
from .views import list_view, add_view, edit_view, person_delete

urlpatterns = [
    url(r'^$', list_view, name='list'),
    url(r'^add/$', add_view, name='add'),
    url(r'^edit/([0-9])/$', edit_view, name='edit'),
    url(r'^delete/([0-9])/$', person_delete, name='delete')
]
