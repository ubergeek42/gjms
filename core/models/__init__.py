#coding: utf8

""" Models. Defining the data structures of GJMS """

import os, sys, elixir, gjms.util.database
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

class User(elixir.Entity):
    """ 
        The User model. Contains all information about a user
        and allows querying. One user can have many games
    """

    name = elixir.Field(elixir.String(40), unique=True)
    password = elixir.Field(elixir.Unicode(512))
    email = elixir.Field(elixir.String(50))

    games = elixir.OneToMany("Game")
    ratings = elixir.OneToMany("Rating")

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

    def __repr__(self):
        return "<Rating %s>" % (self.value)

database = gjms.util.database.setup("tdb5.db")

elixir.setup_all()
elixir.create_all()
