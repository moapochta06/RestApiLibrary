from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer): #создаёт поля на основе атрибутов модели; проверяет данные при сериализации и десериализации; включает методы для создания и обновления экземпляров модели
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'