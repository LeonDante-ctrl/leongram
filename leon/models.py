from time import timezone
from django.db import models
from django.utils import timezone

# image = Profile Photo
# Bio = caption

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null =True)
    caption = models.TextField()
    created_period = models.DateTimeField(default=timezone.now)