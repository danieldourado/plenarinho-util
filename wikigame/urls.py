from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomeGameView.as_view(), name='index'),
    url(r'^list/$', views.WikiGameList.as_view(), name='list'),
    url(r'^extract_data_from_csv/$', views.extract_data_from_csv, name='extract_data_from_csv'),
    url(r'^new/$', views.WikiGameCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.WikiGameDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.WikiGameUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.WikiGameDelete.as_view(), name='delete'),
]
