# The Eye
A service that collects events from applications to help make 
data-driven decisions regarding web analytics.

## Live Demo
This project has a live working demo at
[https://www.the-eye.app/](https://www.the-eye.app/)

**Important** <br>
For login information, please see my email invitation.
When logged in, you will see the features in action.

The demo is consuming an api from a **second** app I wrote for this 
project called "Event Tracker."  This client app is also a live
web application and the code can be found within the "fairysite"
project in my github repositories here:
[Client App Used in The Eye](https://github.com/marcisprouse/fairysite)

## My Conclusions, Rationale and Thought Processes:
This project was completed as a code challenge through a hiring
process.  This section is to elaborate on my conclusions, rationale,
and thought processes for completing the project.
### General:<br>
I immediately knew I would be writing two apps.  One for "The Eye"
and the other, "Event Tracker," for the client talking to "The Eye."
For the **client app**, not "The Eye", I initially thought I would use 
a django package such as django-analytics in order to use a third-party
analytical tool (such as Google Analytics) from an api and consume
that api.  I eventually decided that many of the analytics needed
can be accessed through existing Django middleware and the HTTP
request methods.  I decided to use signals to talk to and update
the model in the client app to get analytic data and I developed
the **Django Rest Framework** within the client app so that I had
an endpoint that can talk to "The Eye."  This app is up and running
(see link above).

For "The Eye", I assumed that this app would take in the client app's
json data and populate models within.  Based on the information within
the project's description, the data and analytics team needed to be
able to query Session, Category, and Time data easily. Due to this
need, I modeled the application accordingly.  The api is retrieved
through a script I wrote within the Management Commands module. This
script is on a schedule to run using a third-party app called django-q,
which is less-complex than django-celery and perfect for this project.
As an option, Django Q can be implemented through the admin panel
which is convenient.  I set up the task this way.  It can be viewed
by logging into the live demo of "The Eye" with the credentials I 
sent. 


### Entities: <br>
It is clear that the project description of the Entities is simpler
than the project actually requires in order to work. It was a great
place to start, though. When monitoring several apps, there needs to 
be a client model. Since the data and analytics team needed to be able
to query Session, Category, and Time data easily, I created their
models and set up the Event model with Session, Category, Time, and
Client as related models (foreign keys).  I ordered the Event model
by the foreign key field's timestamp so that when it is accessed
through the Session model, it will be ordered appropriately. Since
events are associated to a session, it is necessary for the payload
to come in with a session id.  For the client app I created, I
ensured a session was set, even for anonymous users. I validated
for the existence of session_id within "The Eye" model using clean() and
save() overrides. The Client model of "The Eye" is set up by the
user of "The Eye" with token information from the client's app's api
and the endpoint url.  The script runs a for loop over the clients.

I had some idea of what the information coming
in would look like based on the example; however, there was much left
to the imagination.  One of the big questions for me was "Where does
the Category and Name information come from?"  There was a hint for
that answer in the statement: Different types of Events (identified
by category + name) can have different validations for their payloads.
I thought that maybe you can determine the Category and Name based on
the payload of data coming in.  I did this line of thinking within my
script (seed.py) and allowed for an actual Category field and Name
field to come in from the payload as well.

### Constraints and Requirements<br>
The Session, Event, Category, and Time models are populated through
a script I wrote to get the data from the client app's api endpoint.
This script is scheduled and the data is not processed in real time.
I have workers set up through Django Q to keep the data coming in 
asynchronously.  I added the transaction.atomic decorator to my 
seed_event() script with select_for_update to the database calls to
avoid race conditions.

### Use Cases
I implemented the use case of being able to query events for a specific session, certain time ranges, and category.  
I set it up to where GraphQL could query for this information (see examples below). 

**Query Images**

Events by a certain session:
![Image: Example of Query Events by a certain Session](https://www.the-eye.app/static/the_eye/events_by_session.jpg)

Events by time range:
![Image: Example of Query Events by a certain Session](https://www.the-eye.app/static/the_eye/events_by_time_range.jpg)

Events by category:
![Image: Example of Query Events by a certain Session](https://www.the-eye.app/static/the_eye/events_by_category.jpg)


**This query renders all events for a specific session:**
```json
query {allEventsBySessionId(sessionId:"kfo70hfmvt3pfwmgc3tkt0xjbpja1rmu") {
  sessionId
  eventsBySession {
    category {
      name
    }
    name
    data
    timestamp {
      timestamp
    }
  }
}

}
```


**This query renders all events for a certain time range:**
```json
query {allEventsFromDateTo(
  fromDate:"2021-12-31 12:17:32.047892+00:00",
  toDate:"2022-01-03 07:39:23.066994+00:00"
) {
  eventsByTime {
    sessionId {
      sessionId
    }
    category {
      name
    }
    name
    data
  }
}
  
}
```


**This query renders all events for a certain category:**
```json
query {allEventsByCategory(name:"page interaction") {
  eventsByCategory {
    category {
      name
    }
    name
    data
    timestamp {
      timestamp
    }
  }
}
}
```

Also, I created a views.py with generic List and Detail
views so that the Session, Category, and Time Ranges can be easily 
retrieved.  In this way, the event data can be accessed through the 
detail view for each of those models (since they are related fields 
in the Event model). I created a template for Session List and Session
Detail in the Live Demo Site as an example.  The events related to each
session detail is easily retrieved using related name that was set in
the models into the template.

For the use case of monitoring errors that happens in "The Eye,"
I would create a model for Errors and would use the needed validation
on the other models. I would use django signals to populate the Error
model. I could also use the errors that are produced in Django Q
since errors are modeled there.


## Installation Requirements
Includes, but not exclusively:
* Django 4.0
* Python 3.9
* graphene-django 2.15.0
* django-q 1.3.9
* psycopg2 2.9.2

See requirements.txt for full list and dependencies.

## Usage
"The Eye" is a service that gets a client app's api payload of 
web analytical data, processes that data, and provides two ways
to view the data (GraphQL and within Django Templates).

* Log into "The Eye" at [https://www.the-eye.app/](https://www.the-eye.app/)

* Set up a new client in the admin panel with api endpoint and
token information. Access admin panel in navbar.
  
* Data is automatically retrieved from the api and populates the
models in "The Eye."

* Query information using GraphQL.  Query examples provided when
logged into "The Eye."

* If templates set up, List and Detail views are provided in views.py
so that templates can easily render tables of Session, Category, and 
Time information with related event information.  I did set up the
 Session Lookup templates - you can see it in action in the Live Demo.
 When you click on a session, a detail page with table of events is
 populated.    
  
## Notes to Reviewer
* Please be sure to visit the live demo site! Credentials to login
will be sent with invitation to view the code.
* I created a second, client app to talk to "The Eye". Please view 
  that app as well (link to see code is above.)
* I commited updates periodically with thorough comments.  
* Thank you very much for giving me this opportunity to show you
my skills for the possibility of employment.  If you would like for
  me to do anything further on this project to show you more, please
  don't hesitate to ask.
