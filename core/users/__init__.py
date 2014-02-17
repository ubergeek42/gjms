#coding: utf8

""" User model. Add, delete, edit, and interact with users """

import os, sys, elixir, gjms.util.database
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

class User(elixir.Entity):

    """ 
        The User model. Contains all information about a user
        and allows querying.
    """

    name = elixir.Field(elixir.String(40))
    password = elixir.Field(elixir.Unicode(512))
    email = elixir.Field(elixir.String(50))

    def __repr__(self):
        return "<User '%s' (%s)>" % (self.name, self.email)

database = gjms.util.database.setup("tdb1.db")

elixir.setup_all()
elixir.create_all()
