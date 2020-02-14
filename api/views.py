from rest_framework import generics, viewsets, views, status
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer, FortuneSerializer, FortuneGETSerializer
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404

# Create your views here.

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class FortuneView(views.APIView):
    def post(self, request,  *args, **kwargs):
        #print(pk)
        #query = Book.objects.get(pk=pk)
        #print(query)
        #query_data = BookSerializer(instance=query)
        #print(query_data)
        serializer = FortuneSerializer(data=request.data)
        #print(request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

class FortuneGETView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = FortuneGETSerializer(instance=book)
        return Response(serializer.data, status.HTTP_200_OK)
