from tours import tours_data


def departures(request):
    return {
        'departures': tours_data.departures,
    }
