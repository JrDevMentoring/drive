from django.conf.urls import include, url
from django.contrib import admin

from motions import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^login$', views.login, name='login'),
  url(r'^slack/', include('django_slack_oauth.urls')),
  url(r'^motions/', include('motions.urls')),
  url(r'^admin/', admin.site.urls),
]
