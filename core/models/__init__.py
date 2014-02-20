#coding: utf8

""" Models. Define the data structures of GJMS """

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

    def __repr__(self):
        return "<User '%s' (%s)>" % (self.name, self.email)

class Game(elixir.Entity):

    """ 
        The Game model. Contains all information about a game
        and allows querying. Many games can have one user.
    """

    name = elixir.Field(elixir.String(40), unique=True)
    author = elixir.ManyToOne("User")

    def __repr__(self):
        return "<Game '%s' by %s>" % (self.name, self.author.name)


# Set up database and prepare it.
database = gjms.util.database.setup("tdb1.db")

elixir.setup_all()
elixir.create_all()