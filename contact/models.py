from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=70)
    text = models.TextField(null=True) #TODO: delete null 
    #name text instead of message to avoid the same name with message method in antd
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    