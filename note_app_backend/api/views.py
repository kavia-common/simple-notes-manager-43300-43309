from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, pagination, filters
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def health(request):
    """
    Minimal health-check endpoint.
    """
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
class NotePagination(pagination.PageNumberPagination):
    """Page size and number pagination for notes list."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# PUBLIC_INTERFACE
class NoteListCreateView(generics.ListCreateAPIView):
    """
    get:
    Returns a paginated list of notes ordered by updated_at descending.

    post:
    Creates a new note. Requires 'title' field (max 255 chars; required).
    """
    queryset = Note.objects.all().order_by('-updated_at')
    serializer_class = NoteSerializer
    pagination_class = NotePagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated_at']
    ordering = ['-updated_at']

# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a note by ID.

    put:
    Update a note completely.

    patch:
    Update a note partially.

    delete:
    Delete a note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
