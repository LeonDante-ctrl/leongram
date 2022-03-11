from time import timezone
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# image = Profile Photo
# Bio = caption

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null =True)
    caption = models.TextField()
    saved = models.BooleanField(default=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_period = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={"id":self.id})
    
    def __str__(self):
        return self.caption 