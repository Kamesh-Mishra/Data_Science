# Check the validity of a name
import re

def parse_name(input):
	pattern = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Madam\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	match = pattern.search(input)
	print(match.groups())
	print(match.group('first'))
	print(match.group('last'))

parse_name('Mrs. Raveena Tandon')