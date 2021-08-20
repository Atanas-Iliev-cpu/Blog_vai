from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_vai.blogs.urls')),
    path('accounts/', include('blog_vai.accounts.urls')),
    path('comment/', include('blog_vai.comments.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
