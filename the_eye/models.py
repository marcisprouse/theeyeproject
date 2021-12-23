from django.db import models
from django.conf import settings



class Event(models.Model):
    category = models.CharField(max_length=80, blank=True, null=True) # This field will be determined based on the data that comes in from the external api.
    name = models.CharField(max_length=80, blank=True, null=True) # This field will be determined based on the data that comes in from the external api.
    data = models.JSONField(blank=True, null=True) # This field will be populated based on the data field information that comes in from the external api.
    timestamp = models.DateTimeField(blank=True, null=True) # This field will be populated from the "data" field external api, so it is not auto_now_add.

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return "%s %s" %(self.category, self.name)


class Session(models.Model):
    session_id = models.CharField(max_length=255, blank=True, null=True) # This field will be populated based on the data field information that comes in from the external api.
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='sessions')

    def __str__(self):
        return self.session_id


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api_url = models.URLField(max_length=200, blank=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Client: %s   API Endpoint: %s" %(self.user, self.api_url)
