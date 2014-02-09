import re
regex = re.compile("[^@]+@[^@]+\.[^@]+")

def valid(email):
	if regex.match(email):
		return True
	else:
		return False