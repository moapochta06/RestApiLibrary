# Generated by Django 5.0.7 on 2024-11-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('fiction', 'Художественное произведение'), ('textbook', 'Учебник')], default='fiction', max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author', 'publication_year', 'publisher', 'book_type')},
        ),
    ]
