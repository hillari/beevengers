from django.shortcuts import render


def suitable_hives(request):
    return render(request, 'overwintering_in_cold_weather/suitable_hives/suitable_hives.html')


def colony_analysis(request):
    return render(request, 'overwintering_in_cold_weather/colony_analysis/colony_analysis.html')


def nutrition(request):
    return render(request, 'overwintering_in_cold_weather/nutrition/nutrition.html')


def honey_bee_health(request):
    return render(request, 'overwintering_in_cold_weather/honey_bee_health/honey_bee_health.html')


def maintenance(request):
    return render(request, 'overwintering_in_cold_weather/maintenance/maintenance.html')