from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = "tours/index.html"


class DepartureView(TemplateView):
    template_name = 'tours/departure.html'


class TourView(TemplateView):
    template_name = "tours/tour.html"
