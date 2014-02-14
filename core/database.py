import peewee

database = peewee.SqliteDatabase("../dtf")

class connector(peewee.Model):
	class Meta:
		database = database
