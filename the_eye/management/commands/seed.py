import requests
from django.core.management.base import BaseCommand
from the_eye.models import Event, Client, Session, Time, Category
import dateutil.parser
from django.db import transaction

clients = Client.objects.all()

for client in clients:

    def get_data():
        url = str(client.api_url)
        headers = {'Authorization': 'Token ' + str(client.token)}
        r = requests.get(url, headers=headers)
        data = r.json()
        return data


    @transaction.atomic #using to prevent race conditions with select_for_update
    def seed_event():
        idx = 0 # initiate counter for data json object index
        raw_data=get_data()
        for i in get_data():

            # session model
            s = Session.objects.select_for_update().filter(session_id=i['session_id'])
            if s.exists():
                print("Already there.")
            else:
                s = Session.objects.create(session_id=i['session_id'])
                s.save()

            instance_id = int(i['id'])

            # category

            if 'category' in raw_data:
                category = i['category']

            if 'name' in raw_data:
                name = i['name']

            if i['content_type'] == 8:
                category = 'page interaction'  # I am thinking that based on the data, that can determine the category if external api doesn't have one.  If I knew more of the category options, I could add more possibilities.
            else:
                category = 'other interaction'


            c = Category.objects.select_for_update().filter(name=category)
            if c.exists():
                print("Already there.")
            else:
                c = Category.objects.create(name=category)
                c.save()

            if 'click' in raw_data[idx]: # As in above, I am thinking that the data that comes in can determine the name of the event, if a name isn't given in external api.
                name = 'button click'
            else:
                name = 'page viewed'

            raw_data[idx].pop('session_id')
            raw_data[idx].pop('timestamp')
            raw_data[idx].pop('content_type')
            raw_data[idx].pop('id')

            parsed_timestamp = dateutil.parser.parse(i['timestamp']) # making that timestamp from string back to DateTimeField

            t = Time.objects.select_for_update().filter(timestamp=parsed_timestamp)
            if t.exists():
                print("Already there.")
            else:
                t = Time.objects.create(timestamp=parsed_timestamp)
                t.save()

            s = Session.objects.select_for_update().get(session_id=i['session_id'])
            c = Category.objects.select_for_update().get(name=category)
            t = Time.objects.select_for_update().get(timestamp=parsed_timestamp)

            event=Event(
                client = client,
                session_id = s,
                instance_id = instance_id,
                data = raw_data[idx],
                timestamp = t,
                category = c,
                name = name
            )

            idx = idx + 1

            if Event.objects.select_for_update().all().filter(instance_id = int(i['id'])) and Session.objects.select_for_update().all().filter(session_id = i['session_id']): # This is to prevent duplicates
                print("Already there.")
            else:
                event.save()


    class Command(BaseCommand):
        def handle(self, *args, **options):
            seed_event()
            print("completed")

