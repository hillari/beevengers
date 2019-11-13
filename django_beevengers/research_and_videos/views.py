from django.shortcuts import render


def articles(request):
    return render(request, 'research_and_videos/articles/articles.html')


def recommended_publications(request):
    return render(request, 'research_and_videos/recommended_publications/recommended_publications.html')


def recommended_sites(request):
    return render(request, 'research_and_videos/recommended_sites/recommended_sites.html')


def videos(request):
    return render(request, 'research_and_videos/videos/videos.html')
