from django.db import models
from authentication.models import User
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



