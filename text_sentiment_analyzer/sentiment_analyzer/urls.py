from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_text, name='process_text'),
    path('result/', views.result, name='result'),
    path('process_csv/', views.process_csv, name='process_csv'),

]
