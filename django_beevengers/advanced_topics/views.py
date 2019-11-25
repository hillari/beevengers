from django.shortcuts import render


def suitable_hives(request):
    return render(request, 'advanced_topics/suitable_hives/suitable_hives.html')


def colony_analysis(request):
    return render(request, 'advanced_topics/colony_analysis/colony_analysis.html')


def nutrition(request):
    return render(request, 'advanced_topics/nutrition/nutrition.html')


def honey_bee_health(request):
    return render(request, 'advanced_topics/honey_bee_health/honey_bee_health.html')


def maintenance(request):
    return render(request, 'advanced_topics/maintenance/maintenance.html')