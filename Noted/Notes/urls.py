from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:pk>/details', views.note_detail, name='note_detail'),
    path('note/new/', views.create_note, name='note_create'),
    path('note/<int:pk>/edit', views.update_view, name='note_update'),
    path('note/<int:pk>/delete', views.delete_note, name='note_delete'),
]
