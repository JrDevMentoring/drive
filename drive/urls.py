from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^', include('motions.urls')),
  url(r'^motions/', include('motions.urls')),
  url(r'^admin/', admin.site.urls),
]
