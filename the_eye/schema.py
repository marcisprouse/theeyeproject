from graphene_django import DjangoObjectType
import graphene
from .models import Session, Category, Time, Event


class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        fields = ('session_id',)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('name',)


class TimeType(DjangoObjectType):
    class Meta:
        model = Time
        fields = ('timestamp',)


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ('session_id', 'category', 'name', 'data', 'timestamp')


class Query(graphene.ObjectType):
    all_sessions = graphene.List(SessionType)
    all_categories = graphene.List(CategoryType)
    all_times = graphene.List(TimeType)
    all_events = graphene.List(EventType)

    def resolve_all_sessions(root, info):
        return Session.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_times(root, info):
        return Time.objects.all()

    def resolve_all_events(root, info):
        return Event.objects.all()

    session_id = graphene.Field(SessionType)
    events_by_session = graphene.List(EventType,
                                session_id=graphene.ID(),
                                category=graphene.String(),
                                name=graphene.String(),
                                data=graphene.JSONString(),
                                timestamp=graphene.DateTime()
                            )

    def resolve_session_id(self, info, id):
        return Session.objects.get(pk=id)

    def resolve_events_by_session(self, info, session_id=None, category=None, name=None, data=None, timestamp=None, **kwargs):
        if session_id:
            return Event.objects.filter(session_id__id=session_id)

schema = graphene.Schema(query=Query)




