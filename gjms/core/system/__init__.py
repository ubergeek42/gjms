#coding: utf8

"""
    GJMS System.
"""

import os
import sys
import elixir

import gjms.util.database
import gjms.util.url
import gjms.core.exceptions
from gjms.core.models import GJMS

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

def add(name):
    """
        Preferred way to add a system.
    """

    return GJMS.get_by_or_init(id=1, name=name)


def get(id_name):
    """
        Gets a system by the given ID
    """

    system = GJMS.get_by_or_init(id=id_name)
    if type(system) != GJMS:
        raise gjms.core.exceptions.NonExistentPlatform("This system does not exist")
    else:
        return system

gjms_system = get(1)
elixir.session.commit()
