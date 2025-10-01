from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} , {self.last_name}" .title()

class Book(models.Model):

    Title= models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE )

    def __str__(self):
        return self.Title
