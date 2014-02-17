#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import gjms.core.database, gjms.util.password, gjms.core.exceptions, gjms.core.users, peewee, playhouse.kv
class Game(gjms.core.database.connector):
	author = peewee.ForeignKeyField(gjms.core.users.User)
	name = peewee.TextField()
	description = peewee.TextField()
	image = peewee.TextField()
	platforms = playhouse.kv.PickledKeyStore(database=gjms.core.database.database)
	ratings = playhouse.kv.KeyStore(peewee.TextField(null=True), database=gjms.core.database.database)

	def add_platform(self, name, link):
		Game.platforms[name] = link

	def add_rating(self, user, rating):
		Game.ratings[user] = rating

	def get_rating(self):
		counter = 0
		score = 0
		for user, rating in Game.ratings:
			score += float(rating)	
			counter += 1.0
		return float(score / counter)


Game.create_table(fail_silently=True)

def add(game, by, desc, img):
	new_game = Game.create(name=game, author=by, description=desc, image=img)
	print "Added '%s' by %s." % (game, by.name)
	return new_game

def get(gamename):
	try:
		game = Game.get(Game.name == gamename)
	except:
		game = None

	if type(game) is gjms.core.games.Game:
		return game
	else:
		raise gjms.core.exceptions.NonExistentGame, "There is no game with that name."


def by(author):
	games = Game.select(Game, gjms.core.users.User).where(Game.author == author).join(gjms.core.users.User)
	return games