from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   #return render(request, 'pages/homePage.html')
   return HttpResponse("Hello, world. You're at the PAGES index.")
  # return render(request,'index.html', context=context)
