from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from eleitor_mirim.views import ContagemVotos
from projetos.views import ProjetoList

urlpatterns = [
    url(r'^$', ProjetoList.as_view(), name='home'),
    url(r'^apuracao_votos_eleitor_mirim/$', ContagemVotos.as_view(), name='apuracao_votos_eleitor_mirim'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('camara_mirim_util.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^projetos/', include('projetos.urls', namespace='projetos')),
    url(r'^jogo_cidadania/', include('jogo_cidadania.urls', namespace='jogo_cidadania')),
    url(r'^trivia/', include('trivia.urls', namespace='trivia')),
    url(r'^wikigame/', include('wikigame.urls', namespace='wikigame')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
