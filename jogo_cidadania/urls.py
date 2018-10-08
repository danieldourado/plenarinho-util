from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.FalasList.as_view(), name='list'),
    url(r'^new/$', views.FalasCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.FalasDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.FalasUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.FalasDelete.as_view(), name='delete'),
]
