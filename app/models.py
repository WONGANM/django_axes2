from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need here (e.g., profile picture, bio, etc.)

    def __str__(self):
        return self.user.username
