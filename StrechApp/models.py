from django.db import models
from django.urls import reverse

from users_app.models import CustomUser

class exercises(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Bodypart = models.CharField(max_length=50)
    Duration = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Bodypart} - {self.Date} - {self.Duration}'

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('posts:home')