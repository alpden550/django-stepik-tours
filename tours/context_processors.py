import tours.tours_data as tours_data


def departures(request):
    return {
        'departures': tours_data.departures,
    }
