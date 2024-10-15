from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer , NoteSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import Note

class NoteListCreateView(generics.ListCreateAPIView):
    """
    A simple view that allows us to list and create notes

    - Lists all of the notes the user has created or it will create a new note
    """
    # queryset = Note.objects.all() # what objects we want to get from the model
    serializer_class = NoteSerializer # what kind of data we need to accept to make a new note
    permission_classes = [IsAuthenticated] # specifies who can call this - only the ones with JWT

    def get_queryset(self):
        user = self.request.user # get the user who is making the request
        return Note.objects.filter(author=user) # filter the notes by the author of the note

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDeleteView(generics.DestroyAPIView):
    """_summary_
    
    Args:
        generics (_type_): _description_

    Returns:
        _type_: _description_
    """
    #   queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # get the user who is making the request
        return Note.objects.filter(author=user) # filter the notes by the author of the note


class CreateUserView(generics.CreateAPIView):
    """
    A simple view that allows us to create new user
    """
    queryset = User.objects.all() # what objects we want to get from the model , when creating a new user 
    serializer_class = UserSerializer # what kind of data we need to accept to make a new user 
    permission_classes = [AllowAny] # specifies who can call this  , in this case we allow anyone even if they're not authenticated to use this view to create a new user
    