import re
titles = [
	'Significant (1987)',
	'Tales of the city (1978)',
	'The Days of Anna (2000)',
	'Mary ann in autumn (2010)',
	'babycakes (1984)',
]

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
fixed_titles = []

for book in titles:
	result = pattern.sub("\g<date> - \g<title>", book)
	fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)