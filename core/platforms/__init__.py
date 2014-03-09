#coding: utf8

""" 
    Platform interactions. Only basic CRUD.
    Another thing that can be done with a gjms.core.models.Platform
    object is to filter for games on that platform. There's a many-to-many
    relationship with the gjms.core.models.Game object.

    The rest is to be done via a gjms.core.models.Game object.

    To add a platform to a game, you can basically use
    gjms.core.models.Game.platforms as a list.

    Changes have to be commited manually to database.
"""

import os
import sys

import gjms.util.database
import gjms.util.url
import gjms.core.exceptions
from gjms.core.models import Platform


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def add(name, download):
    """ 
        Preferred way to add a platform. 

        Fixes up the download link, if http:// is missing, so you don't 
        accidentally link internally.
    """

    if not "http://" in download:
        download_fixed = "http://"+download
    else:
        download_fixed = download


    if gjms.util.url.validate(download_fixed):
        platform = Platform(name=name, download=download_fixed)
        return platform
    else:
        raise gjms.core.exceptions.InvalidURL("URL not valid.")


def get(id_name):
    """
        Gets a platform by the given filter (either name or ID. Name preferred.) 
    """

    platform = Platform.get_by(name=str(id_name).decode("utf-8"))
    if type(platform) != Platform:
        platform = Platform.get_by(id=id_name)
        if type(platform) != Platform:
            raise gjms.core.exceptions.NonExistentPlatform("Platform does not exist.")
        else:
            return platform
    else:
        return platform


def delete(id_name):
    """ 
        Delete platform. Supply either name, ID or a platform object.
        (Name preferred.)
    """

    if type(id_name) != Platform:
        platform = get(id_name)
        platform.delete()
        print "Platform'%s' deleted." % (platform.name)
    else:
        id_name.delete()
        print "Platform '%s' deleted." % (id_name.name)

