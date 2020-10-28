# This checks the validity of a phone number
import re

def extract_phone(input):
	#phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	phone_regex = re.compile(r'\+\d{2}-\d{10}\b')
	match = phone_regex.findall(input)
	if match:
		return match
	return None

print(extract_phone('this is the num +91-7468643278, +91-2113456789'))

def is_valid_num(input):
	match = re.findall(r'\+\d{2}-\d{10}\b', input)
	if match:
		return True
	return False

print(is_valid_num('+91-7564911835'))