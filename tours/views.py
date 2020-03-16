from django.shortcuts import render
from django.views import View


class MainView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request, departure):
        return render(request, self.template_name)


class TourView(View):
    template_name = "tour.html"

    def get(self, request, tour_id):
        return render(request, self.template_name)
