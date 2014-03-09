"""

    gjms.core.exceptions

    A bunch of custom exceptions for providing useful information
    in case of failure. Also used for unit testing.

"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


# Non-existent objects.
class NonExistentGame(Exception):
    """ Game doesn't exist. """
    pass


class NonExistentUser(Exception): 
    """ User doesn't exist. """
    pass


class NonExistentRating(Exception):
    """ Rating doesn't exist. """
    pass


class NonExistentPlatform(Exception): 
    """ Platform doesn't exist. """
    pass


class NonExistentEvent(Exception):
    """ Event doesn't exist. """
    pass


# Invalid values.bbb
class InvalidEmail(Exception):
    """ E-Mail doesn't match regex """
    pass


class InvalidURL(Exception):
    """ URL doesn't match regex """
    pass


class InvalidValue(Exception):
    """ Value is not of expected type. """
    pass


class InvalidParameter(Exception):
    """ Object passed to function is incorrect. """
    pass
