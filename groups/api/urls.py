from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({
        'get': 'list', 'post': 'create'}),
        name='category_list'),
    path('categories/<int:id>/', CategoryViewSet.as_view({
        'get': 'retrieve','delete': 'destroy',
        'put': 'update', 'patch': 'partial_update'}),
        name='category_detail'),

    path('groups/', GroupViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='group_list'),
    path('groups/<int:id>/', GroupViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy', 'put': 'update',
        'patch': 'partial_update'}),
        name='group_detail'),

]