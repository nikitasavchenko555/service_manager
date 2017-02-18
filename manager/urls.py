from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_issue/', views.create_issue, name='create_issue'),
]
