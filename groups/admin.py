from django.contrib import admin
from . import models
from .models import Category, Group, GroupMember


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember
admin.site.register(models.Group)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
admin.site.register(Category, CategoryAdmin)