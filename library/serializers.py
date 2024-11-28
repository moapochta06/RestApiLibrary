from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        # Проверка уникальности книги
        title = validated_data.get('title')
        author = validated_data.get('author')
        publication_year = validated_data.get('publication_year')
        publisher = validated_data.get('publisher')
        book_type = validated_data.get('book_type')

        if Book.objects.filter(title=title, author=author, publication_year=publication_year,
                               publisher=publisher, book_type=book_type).exists():
            raise serializers.ValidationError("Книга с такими данными уже существует.")

        return super().create(validated_data)


class AuthorSerializer(serializers.ModelSerializer):#создаёт поля на основе атрибутов модели; проверяет данные при сериализации и десериализации; включает методы для создания и обновления экземпляров модели 
    
    books = BookSerializer(many=True, read_only=True)  # Вложенный сериализатор для списка книг

    class Meta:
        model = Author
        fields = '__all__'