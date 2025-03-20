from django.urls import path
from events import views

urlpatterns = [
    path('', views.organizer_dashboard, name='organizer_dashboard'),
    
    path('event/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:event_id>/update/', views.update_event, name='update_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),

    path('participant/', views.participant_list, name='participant_list'),
    path('participant/<int:participant_id>/', views.participant_detail, name='participant_detail'),
    path('participant/create/', views.create_participant, name='create_participant'),
    path('participant/<int:participant_id>/update/', views.update_participant, name='update_participant'),
    path('participant/<int:participant_id>/delete/', views.delete_participant, name='delete_participant'),

    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/<int:category_id>/update/', views.update_category, name='update_category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
]