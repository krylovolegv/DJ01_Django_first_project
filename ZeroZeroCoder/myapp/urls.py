from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('art/', views.new_index, name='new_index'),
    path('training/', views.training_view, name='training'),
    path('events/', views.events_view, name='events'),
]

