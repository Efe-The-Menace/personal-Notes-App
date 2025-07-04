from django.db import models
from django.contrib.auth.models import User

class profile_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    