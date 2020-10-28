import re

pattern = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	# username for email
	@					# @
	([0-9a-z\.-]+)		# email provider
	\.					# .
	([a-z\.]{2,6})$		# com, org, net, etc
	""", re.VERBOSE | re.IGNORECASE)
# re.X | re.I is same as above

match = pattern.search('Priyanshu009ch@gmail.com')
print(match.groups())