from django.db import models
from django.forms import ModelForm


class Books(models.Model):
    title = models.CharField(max_length=500)
    readlink = models.CharField(max_length=500)
    copies = models.IntegerField()
    bookid = models.CharField(max_length=100)

    def __str__(self):
        return self.title,self.copies


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title','readlink','copies',]

# Create your models here.
