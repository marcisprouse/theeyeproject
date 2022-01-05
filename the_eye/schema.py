from graphene_django import DjangoObjectType
import graphene
from .models import Session, Category, Time, Event
from django.utils import dateparse


class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        fields = ('session_id', 'events_by_session')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('name', 'events_by_category')


class TimeType(DjangoObjectType):
    class Meta:
        model = Time
        fields = ('timestamp', 'events_by_time')


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ('session_id', 'category', 'name', 'data', 'timestamp')


class Query(graphene.ObjectType):
    all_sessions = graphene.List(SessionType)
    all_categories = graphene.List(CategoryType)
    all_times = graphene.List(TimeType)
    all_events = graphene.List(EventType)
    all_events_by_session_id = graphene.Field(SessionType, session_id=graphene.String(required=True))
    all_events_from_date_to = graphene.List(
        TimeType,
        from_date=graphene.String(),
        to_date=graphene.String(),
    )
    all_events_by_category=graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_sessions(root, info):
        return Session.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_times(root, info):
        return Time.objects.all()

    def resolve_all_events(root, info):
        return Event.objects.all()

    def resolve_all_events_by_session_id(root, info, session_id):
        try:
            return Session.objects.get(session_id=session_id)
        except Session.DoesNotExist:
            return None

    def resolve_all_events_from_date_to(self, info, **kwargs):
        return Time.objects.filter(
            timestamp__gte=dateparse.parse_datetime(kwargs['from_date']),
            timestamp__lte=dateparse.parse_datetime(kwargs['to_date']),
        )

    def resolve_all_events_by_category(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)




