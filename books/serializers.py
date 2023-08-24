from django.db.models import Avg, Count
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Book, Author, Genre, Review, Favorite



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'rating', 'text']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ReviewOfBookSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'rating', 'text']

class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True)
    author = AuthorSerializer()
    is_favorite = serializers.SerializerMethodField()
    review_set = ReviewOfBookSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
    
    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('rating'))['rating__avg']
        return round(average, 2) if average is not None else None

    def get_total_reviews(self, obj):
        return obj.review_set.count()
    
    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.favorite_set.filter(user=request.user).exists()
        return False

class BookListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True)
    author = AuthorSerializer()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'seo_title', 'genres', 'author', 'average_rating', 'total_reviews', 'is_favorite']

    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('rating'))['rating__avg']
        return round(average, 2) if average is not None else None

    def get_total_reviews(self, obj):
        return obj.review_set.count()
    
    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.favorite_set.filter(user=request.user).exists()
        return False

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'book']