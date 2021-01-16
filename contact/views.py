from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('-contact_date')
    serializer_class = ContactSerializer