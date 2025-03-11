from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Image by {self.user.username} at {self.created_at}"
