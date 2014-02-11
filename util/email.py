import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import re, gjms.core.exceptions
regex = re.compile("[^@]+@[^@]+\.[^@]+")

def valid(email):
	if regex.match(email):
		return True
	else:
		raise gjms.core.exceptions.InvalidEmailFormat, "This e-mail format is not valid."