from django.urls import path

from tours.views import DepartureView, MainView, TourView

app_name = 'tours'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('departure/<str:departure>', DepartureView.as_view(), name='departure'),
    path('tour/<int:tour_id>', TourView.as_view(), name='tour'),
]
