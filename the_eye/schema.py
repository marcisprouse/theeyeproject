from graphene_django import DjangoObjectType
import graphene
from .models import Session, Category, Time, Event


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
    session_by_session_id = graphene.Field(SessionType, session_id=graphene.String(required=True))

    def resolve_all_sessions(root, info):
        return Session.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_times(root, info):
        return Time.objects.all()

    def resolve_all_events(root, info):
        return Event.objects.all()

    def resolve_session_by_session_id(root, info, session_id):
        try:
            return Session.objects.get(session_id=session_id)
        except Session.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)




