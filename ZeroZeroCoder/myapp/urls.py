from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('art/', views.art_view, name='art'),
    path('training/', views.training_view, name='training'),
    path('events/', views.events_view, name='events'),
]

