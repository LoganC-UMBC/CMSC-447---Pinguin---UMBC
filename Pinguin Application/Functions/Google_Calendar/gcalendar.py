from __future__ import print_function
import datetime
from pydrive.auth import GoogleAuth

"""
must edit auth.py in PyDrive for GoogleAuth to work with Google Calendar's APIs

within the directory that calls GoogleAuth a settings.yaml file must be included
with the scope for google calendar. the scope level used to allow every function
to opperate is "https://www.googleapis.com/auth/calendar"


"""


class GoogleCalendar(object):



    def __init__(auth=None):
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
