from django.urls import path
from . import views
# we link this to main url file
urlpatterns = [
    path("notes/",views.NoteListCreateView.as_view(),name="note-list"), # we are using the class based view to handle the request
    path("notes/delete/<int:pk>/",views.NoteDeleteView.as_view(),name="delete-note"),
]
