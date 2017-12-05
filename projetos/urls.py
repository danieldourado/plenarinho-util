from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProjetoList.as_view(), name='list'),
    url(r'^new/$', views.ProjetoCreate.as_view(), name='create'),
    url(r'^extract/$', views.ProjetoCrawl, name='extract'),
    url(r'^(?P<pk>\d+)/$', views.ProjetoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ProjetoUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ProjetoDelete.as_view(), name='delete'),
]
