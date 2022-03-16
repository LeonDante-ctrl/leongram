from time import timezone
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

# image = Profile Photo
# Bio = caption

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null =True)
    caption = models.TextField()
    saved = models.BooleanField(default=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_period = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.caption
    @property
    def published(self):
        created_dates = self.created_date.replace(tzinfo=None)
        Now = datetime.now()
        Now = Now.replace(microsecond=0)
        time_difference = Now - created_dates
        if time_difference.days == 0:
            if int(time_difference.seconds/3600) == 0:
                self.published_date = str(int(time_difference.seconds/60)) + " minutes ago"
            else:
                self.published_date = str(int(time_difference.seconds/3600)) + " hours ago"
        else:
            self.published_date = str(int(time_difference.days)) + " days ago"   
        self.save()
        return self.published_date  