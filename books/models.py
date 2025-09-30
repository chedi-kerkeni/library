from django.db import models

class Book(models.Model):
    Title= models.CharField(max_length=50)

    def __str__(self):
        return self.Title.title()


class Author(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} , {self.last_name}" .title()


