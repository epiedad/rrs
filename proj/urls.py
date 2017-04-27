"""rrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rrs import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.RetreatListView.as_view(), name='retreat_list'),
    url(r'^new-retreat/$', views.RetreatCreateView.as_view(), name='new_retreat'),
    url(r'^retreat/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.RetreatDetailView.as_view(), name='retreat'),
    url(r'^new-session/$', views.SessionCreateView.as_view(), name='new_session'),
    url(r'^session/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.SessionDetailView.as_view(), name='session'),
    url(r'^attend-session/$', views.AttendSessionCreateView.as_view(), name='attend_session'),
    url(r'^attendee/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.AttendeeDetailView.as_view(), name='attendee'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
