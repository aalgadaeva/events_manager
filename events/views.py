from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from actions.utils import create_action
from .models import Event



class EventList(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'events/list_of_events.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all()
        else:
            return Event.objects.all()

class UserEvents(generic.ListView)        :
    model = Event
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

class EventDisplay(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
    
        context['attending'] = self.get_object().attendees.all
        return context


class EventDetail(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = EventDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentCreate.as_view()
        return view(request, *args, **kwargs)


class EventFormMixin(object):
    def form_valid(self, form):
        form.instance.user = self.request.user
        create_action(self.request.user, 'created a new event', form.instance)
        return super().form_valid(form)


class EventCreate(LoginRequiredMixin, SuccessMessageMixin, EventFormMixin, generic.CreateView):
    model = Event
    template_name = 'events/create_form.html'
    fields = ('group', 'name', 'details', 'venue', 'time', 'date')
    context_object_name = 'event'
    success_message = "%(name)s was created successfully"


class EventUpdate(LoginRequiredMixin, SuccessMessageMixin, EventFormMixin, generic.UpdateView):
    model = Event
    template_name = 'events/update_form.html'
    template_name_suffix = '_update_form'
    fields = ('group', 'name', 'details', 'venue', 'time', 'date',)
    success_message = "%(name)s was updated successfully"


class EventDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Event
    template_name = 'events/delete.html'
    success_url = reverse_lazy('events:event-list')
    context_object_name = 'event'
    success_message = "%(name)s was deleted successfully"


@login_required()
def attend_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendee = User.objects.get(username=request.user)
    event.attendees.add(attendee)
    create_action(attendee, 'is attending', event)
    messages.success(request, 'You are now attending {0}'.format(event.name))
    return redirect('events:event-detail', pk=event.pk)


@login_required()
def not_attend_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendee = User.objects.get(username=request.user)
    event.attendees.remove(attendee)
    create_action(attendee, 'no longer attending', event)
    messages.success(request, 'You are no longer attending {0}'.format(event.name))
    return redirect('events:event-detail', pk=event.pk)
