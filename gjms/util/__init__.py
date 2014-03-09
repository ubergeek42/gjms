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