from django.conf.urls import url
from .views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView

urlpatterns = [
    url(r'^$', PersonListView.as_view(), name='list'),
    url(r'^add/$', PersonCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', PersonUpdateView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', PersonDeleteView.as_view(), name='delete')
]
