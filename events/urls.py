from django.urls import path, include
from .views import (EventList, CreateEvent, UserEvents, EventDetail,
                    DeleteEvent)

app_name = 'events'

urlpatterns = [
    path('', EventList.as_view(), name='all'),
    path('new/', CreateEvent.as_view(), name='create'),
    path('by/<username>/', UserEvents.as_view(), name='for_user'),
    path('by/<username>/<int:pk>', EventDetail.as_view(), name='single'),
    path('delete/<int:pk>/', DeleteEvent.as_view(),name='delete'),
]