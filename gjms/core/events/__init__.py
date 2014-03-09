#coding: utf8

"""

    Game model interactions. Add, delete, edit, and interact with games.

    None of the actions are applied immediately. You have to send them to the
    database yourself. Of course this needs a bit more effort on your part, but
    it can save your butt if you accidentally delete a game or something.

"""

import os
import sys
import datetime

import gjms.util.database
import gjms.util.url
import gjms.core.exceptions
from gjms.core.models import Event


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def add(start, end, name, theme="", voting=False):
    """ 

        Preferred way to add an event. 

        Checks for valid datetime formats, raises errors on failure.
        Automatically fills in an empty theme, and sets voting to false.

    """

    if type(start) == datetime.datetime:
        if type(end) == datetime.datetime:
            event = Event(start=start, end=end, name=name, theme=theme, voting=voting)
            return event
        else:
            raise gjms.core.exceptions.InvalidValue("End time must be datetime")
    else:
        raise gjms.core.exceptions.InvalidValue("Start time must be datetime")


def get(id_name):
    """
        Gets an event by the given filter (either name or ID. ID preferred.) 
    """

    event = Event.get_by(name=str(id_name).decode("utf-8"))
    if type(event) != Event:
        event = Event.get_by(id=id_name)
        if type(event) != Event:
            raise gjms.core.exceptions.NonExistentEvent("Event does not exist.")
        else:
            return event
    else:
        return event


def delete(id_name):
    """ 
        Delete event. Supply either name, ID or a event object. (ID preferred.)
    """

    if type(id_name) != Event:
        event = get(id_name)
        event.delete()
        print "Event '%s' deleted." % event.name
    else:
        id_name.delete()
        print "Event '%s' deleted." % id_name.name
