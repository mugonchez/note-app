from django.urls import path
from .views import note_view, note_detail_view, share_note_view, search_notes

app_name = 'note'

urlpatterns = [
    path('notes', note_view, name='note-view'),
    path('notes/<int:id>', note_detail_view, name='note-detail-view'),
    path('notes/<int:id>/share/<int:user_id>', share_note_view, name='share-note-view'),
    path('search', search_notes, name='search-notes')
]
