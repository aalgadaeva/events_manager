from django.contrib import admin
from django.urls import path, include
from .views import (ListGroups, CreateGroup, SingleGroup, JoinGroup, LeaveGroup)

app_name = 'groups'

urlpatterns = [
    path('', ListGroups.as_view(), name='all'),
    path('new/', CreateGroup.as_view(), name='create'),
    path('events/in/<slug:slug>',SingleGroup.as_view(), name='single'),
    path('join/<slug:slug>', JoinGroup.as_view(),name='join'),
    path('leave/<slug:slug>', LeaveGroup.as_view(),name='leave'),
]