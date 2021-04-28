from __future__ import print_function
import datetime
from pydrive.auth import GoogleAuth

"""
must edit auth.py in PyDrive for GoogleAuth to work with Google Calendar's APIs

within the directory that calls GoogleAuth a settings.yaml file must be included
with the scope for google calendar. the scope level used to allow every function
to opperate is "https://www.googleapis.com/auth/calendar"


"""


class Google_Calendar(object):



    def __init__(self, auth=None):
        """gives access to the Google Account given

        :param auth: authorized GoogleAuth instance.
        :type auth: pydrive.auth.GoogleAuth.
        """
        self.auth = auth

    def CreateCalendar(self, calendarTitle=None, timeZone=None):

        """Creates a calendar.
           First account that creates it owns the calendar.

        :param calendarTitle: parameter that determines the title of the calendar
        :type param: str

        :param timeZone: parameter that determines the time zone offset
        :type param:str

        """


        newcalendar = {
            'summary': calendarTitle,
            'timeZone': timeZone

        }

        created_calendar = self.auth.service2.calendars().insert(body=newcalendar).execute()

        return created_calendar['id']

    def DeleteCalendar(self, calendarId=None):
        """deletes the calendar.
           Every account that had the calendar will no longer
           have access to the calendar

        :param calendarId: parameter that google calendar service uses
                           to determine which calendar to opperate within
        :type param: str
        """


        self.auth.service2.calendars().delete(calendarId).execute()


    def AddToCalendarList(self, calendarId=None):
        """Adds the calendar to the associated accounts calendar list

        :param calendarId: parameter that google calendar service uses
                           to determine which calendar to opperate within
        :type param: str
        """


        self.auth.service2.calendarList().insert(calendarId).execute()

    def DeleteFromCalendarList(self, calendarID=None):

        """deletes the calendar from the associated accounts calendar list

        :param calendarId: parameter that google calendar service uses
                           to determine which calendar to opperate within
        :type param: str
        """

        self.auth.service2.calendarList().delete(calendarId).execute()

    def CreateEvent(self, calendarId=None, eventTitle=None, eventDescription=None, startTime=None, endTime=None, timeZone=None):
        """creates the event to be inserted into the associated calendar

        :param calendarId: parameter that google calendar service uses
                           to determine which calendar to opperate within
        :type param: str

        :param eventTitle: parameter that determines the event name
        :type param:str

        :param eventTitle: parameter that determines the event description
        :type param:str

        :param startTime: parameter that determines the event start time
        :type param:str

        :param endTime: parameter that determines the event end time
        :type param:str

        :param timeZone: parameter that determines the time zone offset
        :type param:str

        """

        newEvent = {
            'summary': eventTitle,
            'description': eventDescription,
            'start': {
                'dateTime': startTime,
                'timeZone': timeZone,
            },
            'end': {
                'dateTime': endTime,
                'timeZone': timeZone,
            },
        }

        service.events().insert(calendarId, body=newEvent).execute()

    def DeleteEvent(self, calendarID=None, eventId=None):
        """Deletes an event in the associated calendar

        :param calendarId: parameter that google calendar service uses
                           to determine which calendar to opperate within
        :type param: str

        :param eventId: parameter that google calendar service uses
                        to determine which event to operate within
        :type param:str
        """
        self.auth.service2.events().delete(calendarId, eventId).execute()

        #returns list of events
    def getMonthEvents(self, monthBegin, monthEnd):
        """
        monthBegin and monthEnd has to be in this format for GoogleCalendar to pull informaiton
        '2021-01-01'

        the only things that would need to change are year and month day should always be the first of the current month and first of the next month.

        """
        dateStart = startTime + 'T00:00:00' + 'Z' # 'Z' indicates UTC time
        dateEnd = endTime + 'T00:00:00' + 'Z' # 'Z' indicates UTC time


        months_events = eventsself.auth.service2.events().list(calendarId='primary', timeMin=dateStart, timeMax=dateEnd, singleEvents=True, timeZone='America/New_York', orderBy='startTime').execute()

        events = months_events.get('items', [])

        return events

        """
        example call

            #for event in events:
            #    start = event['start'].get('dateTime', event['start'].get('date'))
            #    print(start,'\n', event['summary'],'\n',event['description'],'\n')

        event is an indexed dictionary entry
        link is to a overview of what the dictionary contains

        https://developers.google.com/calendar/v3/reference/events

        what's printed to console based on a test calendar entry
        2021-04-17T20:30:00-04:00
        Test 1
        Test 1

        """
"""gauth = GoogleAuth()
    #gauth.LocalWebserverAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("Credentials.json")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
    # Save the current credentials to a file
gauth.SaveCredentialsFile("Credentials.json")

c = Google_Calendar(gauth)
id = c.CreateCalendar("new2332")
print(id)
"""