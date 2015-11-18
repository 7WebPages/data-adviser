from __future__ import absolute_import

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'
