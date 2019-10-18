from django.shortcuts import render


def homepage(request):
    return render(request, 'pages/homepage/index.html')


def calendar(request):
    return render(request, 'pages/calendar/calendar.html')


def different_bees(request):
    return render(request, 'pages/different_bees/different_bees.html')


def education(request):
    return render(request, 'pages/education/education.html')


def recommended_sites(request):
    return render(request, 'pages/recommended_sites/recommended_sites.html')