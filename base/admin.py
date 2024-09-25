from django.contrib import admin


from .models import Room, Topic, Message, User\
    
admin.site.register(User)   # This line registers the User model with the Django admin site.
admin.site.register(Room)   # This line registers the Room model with the Django admin site.
admin.site.register(Topic) # This line registers the Topic model with the Django admin site.
admin.site.register(Message)     # This line registers the Message model with the Django admin site.
