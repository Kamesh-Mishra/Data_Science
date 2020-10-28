# Check the validity of a url
import re

pattern = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\=.`#?&//=]*)')

match = pattern.search('http://www.youtube.com/playlist=punjab')
print(f'Protocol : {match.group(1)}')
print(f'Domain : {match.group(2)}')
print(f'Everything Else : {match.group(3)}')
print(match.group())
print(match.groups())