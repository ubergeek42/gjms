#coding: utf8

""" Game model interactions. Add, delete, edit, and interact with games """

import os, sys, elixir, gjms.util.database
from gjms.core.models import Game
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def add(name):
    """ Prefered way to add a game. """

    game = Game(name=name)
    return game

def get(id_name):
    """ Gets a game by the given filter (either name or ID. Name is prefered.) """

    game = Game.get_by(name=str(id_name).decode("utf-8"))
    if type(game) != Game:
        game = Game.get_by(id=id_name)
        if type(game) != Game:
            print "Hmmm. This game doesn't appear to exist."
        else:
            return game
    else:
        return game
