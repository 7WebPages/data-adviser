from __future__ import absolute_import

from django.conf.urls import url

from .views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]
