from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import chat_page, chat_api

urlpatterns = [
    path('admin/', admin.site.urls),

    # página inicial
    path('', chat_page),
    path('chat/', chat_page),

    # API do chatbot
    path('api/chat/', chat_api),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    