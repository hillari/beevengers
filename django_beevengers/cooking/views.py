from django.shortcuts import render


def recipes_with_honey(request):
    return render(request, 'cooking/recipes_with_honey/recipes_with_honey.html')