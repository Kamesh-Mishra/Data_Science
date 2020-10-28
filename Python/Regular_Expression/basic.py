import re

#define regex pattern of phone number
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

#search a string with our pattern
res = pattern.search('Call us at 444 555-8956!')
# search only finds first match
# findall finds all the matches and gives a list

print(res.group())