from django.db import models
from django.conf import settings


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api_url = models.URLField(max_length=200, blank=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Session(models.Model):
    session_id = models.CharField(max_length=255, blank=True, null=True) # This field will be populated based on the data field information that comes in from the external api.
    def __str__(self):
        return self.session_id


class Category(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Time(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return str(self.timestamp)

    class Meta:
        ordering = ['-timestamp']


class Event(models.Model):
    client = models.ForeignKey(Client,
                        on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session,
                        on_delete=models.CASCADE,
                        related_name="events_by_session")
    instance_id = models.SmallIntegerField()
    category = models.ForeignKey(Category,
                        on_delete=models.CASCADE,
                        related_name="events_by_category")
    name = models.CharField(max_length=80, blank=True, null=True) # This field will be determined based on the data that comes in from the external api.
    data = models.JSONField(blank=True, null=True) # This field will be populated based on the data field information that comes in from the external api.
    timestamp = models.ForeignKey(Time,
                        on_delete=models.CASCADE,
                        related_name="events_by_time")

    class Meta:
        order_with_respect_to = 'timestamp'

    def __str__(self):
        return "%s %s" %(self.category, self.name)


