from django.shortcuts import render


def state_of_alaska(request):
    return render(request, 'legal_requirements/state_of_alaska/state_of_alaska.html')


def municipality_of_anchorage(request):
    return render(request, 'legal_requirements/municipality_of_anchorage/municipality_of_anchorage.html')