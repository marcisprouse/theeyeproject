from django.contrib import admin
from .models import Event, Client, Session, Time, Category


admin.site.register(Client)

admin.site.register(Event)

admin.site.register(Session)

admin.site.register(Time)

admin.site.register(Category)