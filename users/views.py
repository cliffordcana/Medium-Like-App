from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import Http404
from .models import CustomUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import json
import facebook

User = get_user_model()


'''class FacebookAuthenticatedUser(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            print('user', user)
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNoTExist:
            raise Http404'''

class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )
    import requests
    print(requests.get('https://developers.facebook.com/docs/graph-api/reference/user/picture/'))
    
class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            print('data', data)
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        data = json.loads(request.body.decode('utf-8'))
        print('data', data)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

