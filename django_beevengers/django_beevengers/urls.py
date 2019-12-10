
# idk if this is the right import for static() function below
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('getting_started/', include('getting_started.urls')),
    path('research_and_videos/', include('research_and_videos.urls')),
    path('advanced_topics/', include('advanced_topics.urls')),
    path('gardening/', include('gardening.urls')),
    path('cooking/', include('cooking.urls')),
    path('legal_requirements/', include('legal_requirements.urls')),
    path('store/', include('store.urls')),
    path('blog/', include('blog.urls')),
    path('captcha/', include('captcha.urls'))

]

#  FIXME this code is for production specifically
# Will need to be modified once in production
# The modification should only be removing the 'if.settings.DEBUG' line
# see - https://techstream.org/Web-Development/Serving-Files-in-Django
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
