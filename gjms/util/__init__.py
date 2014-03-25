#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A module for utilities, which includes password hashing and checking,
database connections and e-mail validation. """

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


# noinspection PyBroadException
def terminal_size():
    """ Get the size of the terminal in which GJMS runs. """
    env = os.environ

    # noinspection PyPep8Naming,PyShadowingNames,PyUnresolvedReferences,PyBroadException
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            import struct
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            fd.close()
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])

def populate_db(entries):
    import gjms.util.report

    import gjms.core.users as users
    import gjms.core.games as games
    import gjms.core.events as events
    import gjms.core.system as system
    import gjms.core.ratings as ratings
    import gjms.core.platforms as platforms

    import datetime
    import elixir

    start1 = datetime.datetime.today() - datetime.timedelta(days=3)
    end1 = datetime.datetime.today() - datetime.timedelta(days=1)

    start2 = datetime.datetime.today() - datetime.timedelta(days=1)
    end2 = datetime.datetime.today() + datetime.timedelta(days=1)

    start3 = datetime.datetime.today() + datetime.timedelta(days=3)
    end3 = datetime.datetime.today() + datetime.timedelta(days=5)

    system = system.get(1)

    event1 = events.add(start1, end1, "Annual Doe Jam #1", "Birds")
    event2 = events.add(start2, end2, "Annual Doe Jam #2", "Birds")
    event3 = events.add(start3, end3, "Annual Doe Jam #3", "Birds")

    system.events.append(event1)
    system.events.append(event2)
    system.events.append(event3)

    for i in range(0, entries):
        user = users.add("John Doe %s" % i, "password", "johndoe@example.com")
        game = games.add("Flappy Doe %s" % i, "A Flappy Bird clone.", "http://hostagamejam.com/media/flappy-doe.png")
        rating = ratings.add(4.0)
        platform1 = platforms.add("Android", "http://hostagamejam.com/media/flappy-doe.apk")
        platform2 = platforms.add("iOS", "http://hostagamejam.com/media/flappy-doe.ipa")

        user.games.append(game)
        user.ratings.append(rating)

        game.ratings.append(rating)
        game.platforms.append(platform1)
        game.platforms.append(platform2)

        event1.participants.append(user)
        event1.games.append(game)

        system.users.append(user)
        system.games.append(game)
        system.ratings.append(rating)
        system.platforms.append(platform1)
        system.platforms.append(platform2)

        elixir.session.commit()

        gjms.util.report.output("%d of %d entries added to database." % (i+1, entries))
    return "%s - %d entries successfully added to database." % (user.system.name, entries)
