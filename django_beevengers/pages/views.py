from django.shortcuts import render


def homepage(request):
   return render(request, 'pages/homepage/index.html')
def calendar(request):
   return render(request, 'pages/calendar/calendar.html')