from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


from .serializers import NoteSerializer
from .models import Note
from authentication.models import User


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def note_view(request):
    #list all authenticated user notes
    if request.method == 'GET':
        notes = Note.objects.filter(owner=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    
    # create note for authenticated user
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            # Assign the current user as the owner of the note
            serializer.validated_data['owner'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticated])
def note_detail_view(request, id):
    
    # Get the note associated with the authenticated user
    note = get_object_or_404(Note, id=id, owner=request.user)
    
    
    # Get the note
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    # update note
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete note
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share_note_view(request, id, user_id):

    # Get the note associated with the authenticated user
    note = get_object_or_404(Note, id=id, owner=request.user)

    # Get the user from the user id supplied
    user = get_object_or_404(User, id=user_id)

    # Create a note associated with this user
    if request.method == 'POST':
        Note.objects.create(owner=user, title=note.title, content=note.content)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_notes(request):
    query = request.query_params.get('q', None)
    if query:
        notes = Note.objects.filter(owner=request.user, title__icontains=query)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Please provide a serch query to continue'}, status=status.HTTP_400_BAD_REQUEST)
    




