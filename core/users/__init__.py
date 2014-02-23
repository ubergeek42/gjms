#coding: utf8

""" 
    User model interactions. Add, delete, edit, and interact with users.

    To update a user, grab the corresponding user object (see get() function),
    and update the value you need by setting that variable.

    None of the actions are applied immediately. You have to send them to the
    database yourself. Of course this needs a bit more effort on your part, but
    it can save your butt if you accidentally delete a user or something.

    Example:

        import elixir, gjms.core.users as users

        user = users.get("Folis")
        user.email = "folis@hostagamejam.com"
        elxir.session.commit()

"""

import os, sys, elixir, gjms.util.database, gjms.util.password, gjms.util.email
from gjms.core.models import User
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def add(name, password, email):
    """ 
        Preferred way to add a user. Checks if the email is valid, and hashes 
        the password the user provides.
    """

    if gjms.util.email.validate(email):
        hashed = gjms.util.password.encrypt(password)
        return User(name=name, password=hashed, email=email)
    else:
        print "This e-mail is invalid."

def get(id_name):
    """ 
        Gets a user by the given filter (either name or ID. Name is preferred.) 
    """

    user = User.get_by(name=str(id_name).decode("utf-8"))
    if type(user) != User:
        user = User.get_by(id=id_name)
        if type(user) != User:
            print "Hmmm. This user doesn't appear to exist."
        else:
            return user
    else:
        return user

def delete(id_name):
    """ 
        Deletes users. Supply either name, ID or a user object. 
        (Name is preferred.)
    """

    if type(id_name) != User:
        user = get(id_name)
        user.delete()
        print "User '%s' deleted." % (user.name)
    else:
        id_name.delete()
        print "User '%s' deleted." % (id_name.name)
