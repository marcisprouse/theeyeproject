import requests
from django.core.management.base import BaseCommand
from the_eye.models import Event, Client, Session
import dateutil.parser

clients = Client.objects.all()

for client in clients:

    def get_data():
        url = str(client.api_url)
        headers = {'Authorization': 'Token ' + str(client.token)}
        r = requests.get(url, headers=headers)
        data = r.json()
        return data

    def seed_event():
        idx = 0
        raw_data=get_data()
        for i in get_data():
            if i['content_type'] == 8:
                category = 'page interaction'
            if 'click' not in raw_data[idx]:
                name = 'pageview'
            raw_data[idx].pop('session_id')
            raw_data[idx].pop('timestamp')
            raw_data[idx].pop('content_type')
            raw_data[idx].pop('id')
            event=Event(
                data = raw_data[idx],
                timestamp = dateutil.parser.parse(i['timestamp']),
                category = category,
                name = name
            )

            session=Session(
                session_id=i['session_id'],
                event=event
            )

            idx = idx + 1
            event.save()
            session.save()


    class Command(BaseCommand):
      def handle(self, *args, **options):
        seed_event()
        print("completed")
