from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "The Eye Admin Panel"
admin.site.site_title = "The Eye Portal"
admin.site.index_title = "Welcome to The Eye Portal!"
