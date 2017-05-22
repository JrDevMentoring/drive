from django.conf.urls import include, url

from . import views

app_name = 'motions'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^slack/', include('django_slack_oauth.urls')),
]
