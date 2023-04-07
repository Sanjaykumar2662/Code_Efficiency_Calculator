from django.urls import path
from.views import index
from . import views

urlpatterns = [
    path("", views.qs1, name="qspage"),
    path("index/",index,name="index"),
    path('efficiency/', views.findeff, name='findeff'),
]
