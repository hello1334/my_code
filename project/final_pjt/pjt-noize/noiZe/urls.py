# noiZe/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/v1/', include('movies.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls'))
]