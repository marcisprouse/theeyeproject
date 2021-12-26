from .models import Event


def events_renderer(request):
    all_events = Event.objects.all().order_by('timestamp')

    return { 'all_events':all_events }

