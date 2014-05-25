from django.conf.urls import patterns, url
from team import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^heatmap/', views.heatmap, name='heatmap'),
        url(r'^register/$', views.register, name='register'))
