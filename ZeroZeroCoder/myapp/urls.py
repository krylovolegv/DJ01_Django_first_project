from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
]

