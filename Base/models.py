from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=60)
    content=models.TextField(max_length=400)
    number=models.CharField(max_length=13)
    
