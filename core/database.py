import peewee

database = peewee.SqliteDatabase("../dtd")

class connector(peewee.Model):
	class Meta:
		database = database
