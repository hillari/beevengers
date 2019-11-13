from django.shortcuts import render


def different_honey_bees(request):
    return render(request, 'getting_started/different_honey_bees/different_honey_bees.html')


def different_hives(request):
    return render(request, 'getting_started/different_hives/different_hives.html')

def recommended_equipment(request):
    return render(request, 'getting_started/recommended_equipment/recommended_equipment.html')

def hive_placement(request):
    return render(request, 'getting_started/hive_placement/hive_placement.html')

def classes(request):
    return render(request, 'getting_started/classes/classes.html')
