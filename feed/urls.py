from django.conf.urls import url
from feed import views

urlpatterns = [
    url('/feed', views.feed, name='feed')
]