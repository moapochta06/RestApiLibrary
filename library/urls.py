from django.urls import path
from .views import AuthorList, BookList, BookDetail, AuthorDetail, PublisherList

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),  
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('publishers/', PublisherList.as_view(), name='pub-list'),

]