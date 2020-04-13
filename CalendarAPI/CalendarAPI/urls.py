from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/calendar', include('MainAPP.urls')),
    path('api-auth/', include("rest_framework.urls")),
    path('rest-auth/', include("rest_auth.urls")),
    path('rest-auth/registration/', include("rest_auth.registration.urls")),
   #  path('accounts', include('allauth.urls')),
]


