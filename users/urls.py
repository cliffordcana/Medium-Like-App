from django.urls import path, include
from .views import UserList, UserDetail
app_name = 'users'

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    #path('facebook-user/', UserList.as_view()),
]

