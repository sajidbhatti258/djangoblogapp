
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('', homepage , name='index'),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('',include('blog.urls',namespace='blog')),
    path('user/',include('users.urls', namespace='user')),
    path('comment/',include('comments.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
