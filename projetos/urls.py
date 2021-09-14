from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProjetoList.as_view(), name='list'),
    url(r'^list_for_pdf/$', views.ProjetoListForPDF.as_view(), name='list_for_pdf'),
    url(r'^extract_endereco_participantes/$', views.ProjetoExtractEnderecoParticipantes, name='extract_endereco_participantes'),
    url(r'^extract_email_participantes/$', views.ProjetoExtractEmail, name='extract_email_participantes'),
    url(r'^extract_dados_participantes/$', views.ProjetoExtractDados, name='extract_dados_participantes'),
    
    url(r'^new/$', views.ProjetoCreate.as_view(), name='create'),
    url(r'^extract/$', views.ProjetoCrawl, name='extract'),
    url(r'^(?P<pk>\d+)/$', views.ProjetoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ProjetoUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ProjetoDelete.as_view(), name='delete'),
]
