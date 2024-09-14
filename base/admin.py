from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

admin.site.register(Room)   # This line registers the Room model with the Django admin site.
admin.site.register(Topic) # This line registers the Topic model with the Django admin site.
admin.site.register(Message)     # This line registers the Message model with the Django admin site.
