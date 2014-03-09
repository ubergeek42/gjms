#coding: utf8

""" 
    gjms.core.ratings

    Rating interactions. Only basic CRUD.
    You can also check all games which have received a rating
    X. The rest can be done from gjms.core.models.Game.ratings

    Changes have to be commited manually to database.
"""

import os
import sys

import gjms.util.database
import gjms.core.exceptions
from gjms.core.models import Rating, Game


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def add(value):
    """ 
        Preferred way to add a rating. 
    """

    if isinstance(value, float):
        rating = Rating(value=value)
        return rating
    else:
        raise gjms.core.exceptions.InvalidValue("Ratings have to be type float")


def get(rid):
    """
        Gets a rating by rID. 
    """

    rating = Rating.get_by(id=rid)
    if type(rating) != Rating:
        raise gjms.core.exceptions.NonExistentRating("Rating does not exist")
    else:
        return rating


def delete(rid):
    """ 
        Delete rating by rID.
    """

    rating = get(rid)
    rating.delete()

    print "Rating deleted."


def calculate(game):
    """
        Calculate the rating of a game.
    """

    if type(game) != Game:
        raise gjms.core.exceptions.InvalidParameter("Pass a Game object.")
    else:
        counter = 0.0
        game_rating = 0.0

        for rating in game.ratings:
            game_rating += rating.value
            counter += 1.0

        return game_rating / counter

