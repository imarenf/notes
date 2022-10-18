from django.contrib import admin
from django.urls import path, include

from notes.views import home_page_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('notes.urls')),
    path('', home_page_redirect)
]
