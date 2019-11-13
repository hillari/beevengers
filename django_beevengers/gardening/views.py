from django.shortcuts import render


def pollinator_friendly_vegetation(request):
    return render(request, 'gardening/pollinator_friendly_vegetation/pollinator_friendly_vegetation.html')