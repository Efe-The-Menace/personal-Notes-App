from django.db import models
from django.contrib.auth.models import User

class Note_data(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time_posted = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    