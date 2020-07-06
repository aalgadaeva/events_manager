from rest_framework import viewsets
from .serializers import CategorySerializer, GroupSerializer
from ..models import *
from rest_framework.views import APIView

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    lookup_field = 'id'
    queryset = Category.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    lookup_field = 'id'
    queryset = Group.objects.all()

# class FeedCreate(CreateView):
#     model = Discussion
#     fields = ['text']

#     def form_valid(self, form):
#          obj = form.save(commit=False)
#          obj.name= self.request.user.username
#          obj.save()        
#          return http.HttpResponseRedirect(self.get_success_url())
