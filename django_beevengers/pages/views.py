from django.shortcuts import render, redirect


def redirect_view(request):
    return redirect('home/')

def homepage(request):
    return render(request, 'pages/homepage/index.html')

def store(request):
    return render(request, 'pages/store/store.html')

def calendar(request):
    return render(request, 'pages/calendar/calendar.html')
def articles(request):
    return render(request, 'pages/articles/articles.html')
def education(request):
    return render(request, 'pages/education/education.html')
def videos(request):
    return render(request, 'pages/videos/videos.html')


def education(request):
    return render(request, 'pages/education/education.html')


def recommended_sites(request):
    return render(request, 'pages/recommended_sites/recommended_sites.html')


def legal(request):
    return render(request, 'pages/legal/legal.html')


def community(request):
    return render(request, 'pages/community/community.html')
