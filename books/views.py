from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters

from .models import Book, Author, Genre, Review, Favorite
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ReviewSerializer, ReviewCreateSerializer, FavoriteSerializer, BookListSerializer

class BookFilter(FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    publication_date = filters.DateFromToRangeFilter(field_name='publication_date')

    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'publication_date']

class BookView(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genres', 'author']
    filterset_class = BookFilter
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        value = kwargs['pk']
    
        try:
            if value.isdigit():
                book = queryset.get(id=value)
            else:
                book = queryset.get(seo_title=value)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=404)    
        
        serializer = self.get_serializer(book, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def favorite(self, request, pk=None):
        book = self.get_object()
        if request.user.is_anonymous:
            return Response({'error': 'You must be authenticated'}, status=403)
        Favorite.objects.get_or_create(user=request.user, book=book)
        return Response({'detail': 'Book added to favorites'})

    @action(detail=True, methods=['get'])
    def unfavorite(self, request, pk=None):
        book = self.get_object()
        if request.user.is_anonymous:
            return Response({'error': 'You must be authenticated'}, status=403)
        Favorite.objects.filter(user=request.user, book=book).delete()
        return Response({'detail': 'Book removed from favorites'})

class AuthorModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class GenreModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return super().get_serializer_class()

    @staticmethod
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class FavoriteModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer