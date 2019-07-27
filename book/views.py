from django.shortcuts import render

# Create your views here.
from book.serializers import BooksSerializer
from book.models import Books
from rest_framework.viewsets import ModelViewSet


class BookOperations(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer