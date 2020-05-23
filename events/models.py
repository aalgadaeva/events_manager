from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Event(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='events', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    venue = models.CharField(max_length=200)
    date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('events:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
