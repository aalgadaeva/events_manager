from django.urls import path, include
from .views import EventList, UserEvents, EventDisplay, EventDetail, EventFormMixin, EventCreate, EventUpdate, EventDelete, attend_event, not_attend_event

app_name = 'events'

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/new/', EventCreate.as_view(), name='event-create' ),
    path('by/<username>/', UserEvents.as_view(), name='for_user'),
    path('events/<int:pk>/delete', EventDelete.as_view(), name='event-delete'),
    path('events/<int:pk>/update', EventUpdate.as_view(), name='event-update'),
    path('events/<event_id>/attend/', attend_event, name='attend_event'),
    path('events/<event_id>/not_attend/', not_attend_event, name='not_attend_event'),

]