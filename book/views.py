from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# context for linking the image on api view
class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all()
        serializers = BookSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(fav=True)
        serializers = BookSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UpdateFavData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostModelData(APIView):
    def post(self, request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Book.objects.filter(store_name__contains=search)
        serializers = BookSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def delete(self, request, pk):
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
