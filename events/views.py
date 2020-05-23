from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class EventList(SelectRelatedMixin, generic.ListView):
    model = models.Event
    select_related = ('user','group')
 

class UserEvents(generic.ListView)        :
    model = models.Event
    template_name = 'events/user_event_list.html'

    def get_queryset(self):
        try:
            self.event_user = User.objects.prefetch_related('events').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.event_user.events.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_user'] = self.event_user
        return context

class EventDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Event
    select_related = ('user','group', 'message', 'venue', 'date', 'time')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreateEvent(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('group', 'message', 'venue', 'date', 'time')
    model = models.Event

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteEvent(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Event
    select_related = ('user', 'group')
    success_url = reverse_lazy('events:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request,'Event Deleted')
        return super().delete(*args,**kwargs)



