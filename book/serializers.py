

from rest_framework.serializers import ModelSerializer
from book.models import Books

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

print('inside books models....!.......!')