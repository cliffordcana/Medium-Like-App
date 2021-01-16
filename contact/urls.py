from django.urls import path
from .views import ContactListView

app_name = 'contact'

urlpatterns = [
    path('contact-me/', ContactListView.as_view())
]
