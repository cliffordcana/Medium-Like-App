from django.urls import path
from .views import CategoryListView
from .models import Category
from .serializers import CategorySerializer

app_name = 'category'

urlpatterns = [
    path('categories/', CategoryListView.as_view())
]