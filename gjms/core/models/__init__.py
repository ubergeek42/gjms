#coding: utf8

"""

    gjms.core.models

    All the data structures of GJMS.

"""

import os
import sys

import elixir

import gjms.util.database
from gjms.config import parser

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
elixir.options_defaults.update(dict(tablename=lambda cls: cls.__name__.lower()))

def get_by_or_init(cls, if_new_set={}, **params):
    """Call get_by; if no object is returned, initialize an
    object with the same parameters.  If a new object was
    created, set any initial values."""

    result = cls.get_by(**params)
    if not result:
        result = cls(**params)
        result.set(**if_new_set)
    return result

elixir.Entity.get_by_or_init = classmethod(get_by_or_init)

class User(elixir.Entity):
    """
        The User model. Contains all information about a user
        and allows querying. One user can have many games
    """
    name = elixir.Field(elixir.String(40), unique=True)
    password = elixir.Field(elixir.String(512))
    email = elixir.Field(elixir.String(50))

    participated = elixir.ManyToMany("Event")
    games = elixir.OneToMany("Game")
    ratings = elixir.OneToMany("Rating")

    system = elixir.ManyToOne("GJMS")

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def __repr__(self):
        return "<User '%s' (%s)>" % (self.name, self.email)


class Game(elixir.Entity):
    """
        The Game model. Contains all information about a game
        and allows querying. Many games can have one user.
    """

    name = elixir.Field(elixir.String(40), unique=True)
    description = elixir.Field(elixir.String(512))
    image = elixir.Field(elixir.String(512))

    author = elixir.ManyToOne("User")
    platforms = elixir.ManyToMany("Platform")
    ratings = elixir.ManyToMany("Rating")
    event = elixir.ManyToOne("Event")

    system = elixir.ManyToOne("GJMS")

    def __repr__(self):
        return "<Game '%s' by %s>" % (self.name, self.author.name)


class Platform(elixir.Entity):
    """
        The Platform model. Contains the platform name and a download link.
        Allows for querying the platforms of a game, and all games of a
        platform. Many games can have many platforms.
    """

    name = elixir.Field(elixir.String(40))
    download = elixir.Field(elixir.String(512))
    games = elixir.ManyToMany("Game")

    system = elixir.ManyToOne("GJMS")

    def __repr__(self):
        return "<Platform '%s' (%s)>" % (self.name, self.download)


class Rating(elixir.Entity):
    """
        The Rating model. Contains the a rating value.
        This value can be applied to a game and a user.
        Allows for checking game ratings and ratings a user has given.
    """

    value = elixir.Field(elixir.Float(4))
    games = elixir.ManyToMany("Game")
    user = elixir.ManyToOne("User")

    system = elixir.ManyToOne("GJMS")

    def __repr__(self):
        return "<Rating %s>" % self.value


class Event(elixir.Entity):
    """
        The Event model. Contains all information regarding an event.
        This includes from when to when it's happening, the submitted games,
        and which users participated. Includes the theme.

        Many events can have many users and many games.
    """

    start = elixir.Field(elixir.DateTime(512))
    end = elixir.Field(elixir.DateTime(512))

    name = elixir.Field(elixir.String(512))
    theme = elixir.Field(elixir.String(256))
    voting = elixir.Field(elixir.Boolean())
    comments = elixir.Field(elixir.Boolean())

    games = elixir.OneToMany("Game")
    participants = elixir.ManyToMany("User")

    system = elixir.ManyToOne("GJMS")

    def __repr__(self):
        return "<Event '%s' (%s - %s)>" % (self.name, self.start, self.end)

class GJMS(elixir.Entity):
    """
        The GJMS model. It contains references to all the other models.
        Allows for easy listing of various things.
    """
    name = elixir.Field(elixir.String(32))

    users = elixir.OneToMany("User")
    games = elixir.OneToMany("Game")
    platforms = elixir.OneToMany("Platform")
    ratings = elixir.OneToMany("Rating")
    events = elixir.OneToMany("Event")

    def __repr__(self):
        return "<GJMS - It's alive>"


gjms.util.database.setup(gjms.config.parser.get("gjms", "db_url"))

elixir.setup_all()
elixir.create_all()
