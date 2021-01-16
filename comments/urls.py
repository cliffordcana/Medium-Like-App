from django.urls import path
from .views import CommentList, CommentDetail

app_name = 'comments'

urlpatterns = [
    path('comments/', CommentList.as_view()),
    path('comments/<pk>/', CommentDetail.as_view()),
    #path('comments/<str:slug>/', CommentDetail.as_view()),
]
