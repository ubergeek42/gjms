#coding: utf8

"""

    Game model interactions. Add, delete, edit, and interact with games.

    None of the actions are applied immediately. You have to send them to the
    database yourself. Of course this needs a bit more effort on your part, but
    it can save your butt if you accidentally delete a game or something.

"""

import os
import sys
import slugify

import gjms.util.url
import gjms.util.database
import gjms.core.exceptions

from gjms.core.models import Game

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

def add(name, description, image):
    """
        Preferred way to add a game.

        Fixes up the image link, if http:// is missing, so you don't
        accidentally link internally.
    """

    if not "http://" in image:
        image_fixed = "http://"+image
    else:
        image_fixed = image

    if gjms.util.url.validate(image_fixed):
        slug = slugify.slugify(name)

        game = Game(slug=slug, name=name, description=description, image=image_fixed)
        return game
    else:
        raise gjms.core.exceptions.InvalidURL("URL not valid.")


def by_slug(slug):
    """
        Get a game by its slug.
    """

    game = Game.get_by(slug=slug)
    if type(game) != Game:
        raise gjms.core.exceptions.NonExistentGame("Game with this slug does not exist.")
    else:
        return game

def get(id_name):
    """
        Gets a game by the given filter (either name or ID. Name preferred.)
    """

    game = Game.get_by(name=str(id_name).decode("utf-8"))
    if type(game) != Game:
        game = Game.get_by(id=id_name)
        if type(game) != Game:
            raise gjms.core.exceptions.NonExistentGame("Game does not exist.")
        else:
            return game
    else:
        return game


def delete(id_name):
    """
        Delete game. Supply either name, ID or a game object. (Name preferred.)
    """

    if type(id_name) != Game:
        game = get(id_name)
        game.delete()
        print "Game '%s' deleted." % game.name
    else:
        id_name.delete()
        print "Game '%s' deleted." % id_name.name
