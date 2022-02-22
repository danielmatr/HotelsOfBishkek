from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from main.views import PostViewSet
from .yasg import urlpatterns as doc_url
schema_view = get_swagger_view(title='Pastebin API')
router = DefaultRouter()
router.register('list', PostViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('api/v1/', include("main.urls")),
    path('api/v1/', include('comment.urls')),
    path('', include(router.urls))
]
urlpatterns += doc_url
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
