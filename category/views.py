from rest_framework import generics, permissions, status
from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )
    
    def list(self, request): #TODO: UPDATE THE CATEGORY AUTMATICALLY EVERYTIME A NEW ARTICLE IS ADDEED
        try:
            queryset = self.get_queryset()
            serializer = CategorySerializer(queryset, many=True)
            return Response(serializer.data)
        except self.DoesNotExist:
            return Response('Article not found', status=status.HTTP_404_NOT_FOUND)   