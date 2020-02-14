from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn')


class FortuneSerializer(serializers.Serializer):
    #bookのtitleとisbnが自動で入る
    title = serializers.CharField()
    isbn = serializers.CharField()
    fortune = serializers.SerializerMethodField()
    
    def get_fortune(self, obj):
        return str(obj['title']) + "のisbnは" + str(obj['isbn'])
    
class FortuneGETSerializer(serializers.Serializer):
    #title = serializers.CharField()
    #isbn = serializers.CharField()
    title = serializers.CharField()
    fortune = serializers.SerializerMethodField()
    
    def get_fortune(self, obj):
        return str(obj.title) + "のisbnは" + str(obj.isbn)