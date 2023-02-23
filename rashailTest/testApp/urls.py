from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('last_dose/<str:machine_id>/', views.last_dose, name='last_dose'),
    path('last_dose', views.last_dose_from_html, name='last_dose_from_html'),
]