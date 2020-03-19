import random

from django.http import Http404
from django.views.generic.base import TemplateView

import tours.tours_data as tours_data


class MainView(TemplateView):
    template_name = "tours/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        context['tours'] = random.sample(tours_data.tours.items(), 6)
        return context


class DepartureView(TemplateView):
    template_name = 'tours/departure.html'


class TourView(TemplateView):
    template_name = "tours/tour.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TourView, self).get_context_data(*args, **kwargs)
        tour = tours_data.tours.get(context['tour_id'])
        if tour is None:
            raise Http404
        context['tour'] = tour
        context['departure'] = tours_data.departures.get(tour['departure']).split()[-1]
        return context
