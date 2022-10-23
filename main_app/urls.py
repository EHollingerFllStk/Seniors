from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agencies/', views.agencies_index, name='index'),
    path('agencies/<int:agency_id>/', views.agencies_detail, name='detail'),
    path('agencies/create/', views.AgenciesCreate.as_view(), name='agencies_create'),
    path('agencies/<int:pk>/update/', views.AgenciesUpdate.as_view(), name='agencies_update'),
    path('agencies/<int:pk>/delete/', views.AgenciesDelete.as_view(), name='agencies_delete'),
    path('agencies/<int:agency_id>/add_adds/', views.add_adds, name='add_adds'),
    path('accounts/signup/', views.signup, name='signup'),
]
