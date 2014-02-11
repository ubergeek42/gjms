import peewee

database = peewee.SqliteDatabase("../data.db")

class connector(peewee.Model):
	class Meta:
		database = database
