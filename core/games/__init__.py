#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import gjms.core.database, gjms.util.password, gjms.core.exceptions, gjms.core.users, peewee

class Game(gjms.core.database.connector):
	author = peewee.ForeignKeyField(gjms.core.users.User)
	name = peewee.TextField()

Game.create_table(fail_silently=True)

def add(game, by):
	new_game = Game.create(name=game, author=by)
	print "Added '%s' by %s." % (game, by.name)
	return new_game

def by(author):
	games = Game.select(Game, gjms.core.users.User).where(Game.author == author).join(gjms.core.users.User)
	return games