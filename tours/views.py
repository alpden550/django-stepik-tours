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

    def get_context_data(self, *args, **kwargs):
        context = super(DepartureView, self).get_context_data(*args, **kwargs)
        departure = context.get('departure')

        if departure not in tours_data.departures:
            raise Http404

        tours = {
            tour_id: tour_data
            for tour_id, tour_data in tours_data.tours.items()
            if tour_data['departure'] == departure
        }

        context['tours'] = tours
        context['departure'] = tours_data.departures.get(departure).split()[-1]
        context['tours_prices'] = sorted([tour['price'] for tour in tours.values()])
        context['tours_nights'] = sorted([tour['nights'] for tour in tours.values()])
        return context


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
