"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('terms', TemplateView.as_view(template_name='terms.html'), name='terms'),
    path('ccp', TemplateView.as_view(template_name='ccp.html'), name='ccp'),
    path('sso/', include('apps.esi.urls', namespace='esi')),
    path('accounts/', include('allauth.urls')),
    path('teams/', include('organizations.urls')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('market/', include('apps.market.urls', namespace='market')),
    path('admin/', admin.site.urls),
]

if not settings.TEST:
    urlpatterns = [*urlpatterns, path('', include('django_prometheus.urls'))]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    if 'debug_toolbar' in settings.INSTALLED_APPS and settings.TEST is not True:
        import debug_toolbar

        urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), *urlpatterns]
