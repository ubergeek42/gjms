#coding: utf8

""" User model interactions. Add, delete, edit, and interact with users """

import os, sys, elixir, gjms.util.database
from gjms.core.models import User
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def add(name, password, email):
    """ Preferred way to add a user. Checks if the email is valid, and hashes the password """
    import gjms.util.password, gjms.util.email

    if gjms.util.email.validate(email):
        hashed = gjms.util.password.encrypt(password)
        return User(name=name, password=hashed, email=email)
    else:
        print "This e-mail is invalid."

def get(id_name):
    """ Gets a user by the given filter (either name or ID. Name is preferred.) """

    user = User.get_by(name=str(id_name).decode("utf-8"))
    if type(user) != User:
        user = User.get_by(id=id_name)
        if type(user) != User:
            print "Hmmm. This user doesn't appear to exist."
        else:
            return user
    else:
        return user
