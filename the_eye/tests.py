from django.test import TestCase, TransactionTestCase
from io import StringIO
from django.core.management import call_command
from the_eye.models import Client, Event, Session, Category, Time

class SeedDatabaseFromAppTests(TransactionTestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "seed",
            *args,
            stdout=StringIO(),
            stderr=StringIO(),
            **kwargs,
        )

    def setUpTestData(cls):
        cls.client = Client.objects.create(user='WebfairyClient',
                            api_url='https://www.webfairydesign.com/apievent/?format=json',
                            token='631ca0fd3810547274931c102c58cc6f12c6405b',
                            )
        cls.session_id = Session.objects.create(session_id='kfo70hfmvt3pfwmgc3tkt0xjbpja1rmu')
        cls.category = Category.objects.create(name='page interaction')
        cls.time = Time.objects.create(timestamp='2022-01-17 00:13:25.934073+00:00')
        cls.event = Event.objects.create(client=cls.client,
                                            session_id=cls.session_id,
                                            instance_id=4,
                                            category=cls.category,
                                            name='page view',
                                            data={"ip_address":"68.105.143.72",
                                                    "host":"www.webfairydesign.com",
                                                    "path":"/blog/2021/6/14/power-python-and-django/",
                                                    "object_id":4,
                                                    "user":16
                                                    },
                                            timestamp=cls.time
                                        )


    def test_session_exists(self):
        self.call_command()
        self.assertEqual(self.session_id, 'kfo70hfmvt3pfwmgc3tkt0xjbpja1rmu')

