from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_vai.blogs.urls')),
    path('accounts/', include('blog_vai.accounts.urls')),
    # path('', include('blog_vai.comments.urls')),
]
