from peewee import *

database = SqliteDatabase("../data.db")

class connector(Model):
	class Meta:
		database = database
