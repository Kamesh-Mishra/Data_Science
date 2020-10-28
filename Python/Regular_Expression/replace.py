import re

text = 'Last night Mr. Tarun and Mrs. Khanna played well with Mr. Harman'
pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result = pattern.sub('\g<1> \g<2> ', text)
print(result)