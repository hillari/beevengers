from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('getting_started/', include('getting_started.urls')),
    path('research_and_videos/', include('research_and_videos.urls')),
    path('overwintering_in_cold_weather/', include('overwintering_in_cold_weather.urls')),
    path('gardening/', include('gardening.urls')),
    path('cooking/', include('cooking.urls')),
]
