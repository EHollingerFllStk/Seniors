from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agencies/', views.agencies_index, name='index'),
    path('agencies/<int:agency_id>/', views.agencies_detail, name='detail'),
    path('agencies/create/', views.AgenciesCreate.as_view(), name='agencies_create'),
]