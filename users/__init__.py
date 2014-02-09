#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import gjms.util.database, gjms.util.password, peewee

class User(gjms.util.database.connector):
	name = peewee.TextField()
	password = peewee.TextField()
	email = peewee.TextField()

User.create_table(fail_silently=True)

def add(username, passwrd, mail):
	hashed = gjms.util.password.hash(passwrd)
	new_user = User.create(name=username, password=hashed, email=mail)
	print "User %s created." % username
	return new_user

def delete(username):
	del_user = User.get(User.name == username)
	del_user.delete_instance()
	print "User %s deleted." % username
