"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from snippet import views as snippet_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', snippet_views.homepage, name="homepage"),
    path('snippet/<int:pk>/', snippet_views.snippet_detail, name='snippet_detail'),
    path('snippet/create/', snippet_views.snippet_create, name="snippet_create"),
    path('edit/<int:pk>/', snippet_views.snippet_edit, name="snippet_edit"),
    path('snippet/<int:pk>/delete/', snippet_views.snippet_delete, name="snippet_delete"),
    path('snippet/languages/', snippet_views.lang_add, name="lang_add"),
    path('accounts/', include('registration.backends.default.urls')),
    #path('snippet/<slug:slug>/', snippet_views.snippet_by_lang, name='snippet_by_lang'), 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
