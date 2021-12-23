from django.contrib import admin
from .models import Event, Client, Session


admin.site.register(Client)

admin.site.register(Event)

admin.site.register(Session)
