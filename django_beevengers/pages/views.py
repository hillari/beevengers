from django.shortcuts import render, redirect


def redirect_view(request):
    return redirect('home/')


def homepage(request):
    return render(request, 'pages/homepage/index.html')


def calendar(request):
    return render(request, 'pages/calendar/calendar.html')


def education(request):
    return render(request, 'pages/education/education.html')

