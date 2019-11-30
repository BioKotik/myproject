from django.conf.urls import url
from myapp import views

urlpatterns = [
    url('myapp/', views.index, name='myapp'),
    url('table/', views.table, name='table')
]