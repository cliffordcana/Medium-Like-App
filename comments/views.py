
from rest_framework.views import APIView
from rest_framework import permissions, status, generics, viewsets, mixins
from .serializers import CommentSerializer, CommentDetailSerializer
from rest_framework.response import Response
from .models import Comment
from django.shortcuts import get_object_or_404
from articles.models import Articles
from django.http import HttpResponseBadRequest, Http404
from rest_framework.decorators import api_view
from articles.serializers import ArticlesSerializer

class CommentList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            print(request.data)
            qs = Comment.objects.all().order_by('-comment_date')
            serializer = CommentSerializer(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Comment.DoesNotExist:
            return Response('Comment not found', status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        #print(user)
        print('self.request.user', request.data)
        print('self.request.user', request.user.first_name)

        article_id = data['articleID']
        article = get_object_or_404(Articles, id=article_id)

        comment = data['comment']
        nickname = data['nickname']

        create_comment = Comment.objects.create(
            article=article,
            user=user,
            comment=comment,
            #nickname=nickname
        )
        create_comment.save()
        return Response('Comment created', status=status.HTTP_201_CREATED)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        try:
            return Comment.objects.all().order_by('-comment_date')
        except Comment.DoesNotExist:
            raise Http404

    '''def perform_create(self):
        return self.request.user'''