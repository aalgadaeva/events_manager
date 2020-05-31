from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from tinymce.models import HTMLField
from django.contrib.auth.models import User



class Event(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='events', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    details = HTMLField('Details')
    venue = models.CharField(max_length=200)
    date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attending', blank=True)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)

    
    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['date', 'time']

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def get_number_of_attendees(self):
        return self.attendees.all().count()

 
