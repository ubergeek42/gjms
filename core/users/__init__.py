#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import gjms.core.database, gjms.util.password, gjms.util.email, gjms.core.exceptions, peewee

class User(gjms.core.database.connector):
	name = peewee.TextField()
	password = peewee.TextField()
	email = peewee.TextField()

User.create_table(fail_silently=True)

def get(username):
	try:
		user = User.get(User.name == username)
	except:
		user = None

	if type(user) is gjms.core.users.User:
		return user
	else:
		raise gjms.core.exceptions.NonExistentUser, "There is no user with that username."

def add(username, passwrd, mail):
	if gjms.util.email.valid(mail):
		hashed = gjms.util.password.hash(passwrd)
		new_user = User.create(name=username, password=hashed, email=mail)
		print "User %s created." % username
		return new_user
	else:
		raise gjms.core.exceptions.InvalidEmailFormat, "The given e-mail address has an invalid format."

def delete(username):
	try:
		del_user = User.get(User.name == username)
	except:
		del_user = None

	if type(del_user) is gjms.core.users.User:
		del_user.delete_instance()
		print "User %s deleted." % username
	else:
		raise gjms.core.exceptions.NonExistentUser, "There is no user with that username."


"""
	func login:

	First checks if a user with the given username
	exists. If this is not the case, it raises a
	NonExistentUser exception.

	If it passes, it checks if the given password
	matches the user's hashed password. If it does
	it prints out "Logged in"

	TODO:
		- Make function set user login status.
		- Add decorator to easily determine login status.

"""
def login(username, password):
	try:
		login_user = User.get(User.name == username)
	except:
		login_user = None

	if type(login_user) is gjms.core.users.User:
		if gjms.util.password.check(password, login_user.password):
			print "Logged in!"
		else:
			raise gjms.core.exceptions.IncorrectPassword, "The password you provided is incorrect."
	else:
		raise gjms.core.exceptions.NonExistentUser, "There is no user with that username."