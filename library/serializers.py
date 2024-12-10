# //преобразовывает модели Djago в простые типы (словари, формат JSON)//
#  сериализаторы проверяют корректность данных и могут выдавать ошибки, если данные не соответствуют ожиданиям
# позволяют быстро определять, какие поля должны быть включены в ответ                             

from rest_framework import serializers
from .models import Author, Book, Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    publishers = serializers.PrimaryKeyRelatedField(many=True, queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'publication_year',
            'genre',
            'category',
            'publishers',
            'cover_image',
            'file',
            'book_type'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']