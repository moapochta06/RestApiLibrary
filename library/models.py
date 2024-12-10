from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    BOOK_TYPES = (
        ('fiction', 'Художественное произведение'),
        ('textbook', 'Учебник'),
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100)
    publishers = models.ManyToManyField(Publisher, blank=True, related_name='books') 
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    file = models.FileField(upload_to='books/', blank=True, null=True)
    book_type = models.CharField(max_length=10, choices=BOOK_TYPES, default='fiction')

    class Meta:
        unique_together = ('title', 'author') 

    def __str__(self):
        return self.title