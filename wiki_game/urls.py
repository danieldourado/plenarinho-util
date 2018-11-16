from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.WikiGameList.as_view(), name='list'),
    url(r'^new/$', views.WikiGameCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.WikiGameDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.WikiGameUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.WikiGameDelete.as_view(), name='delete'),
]
