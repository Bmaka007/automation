#(^[a-zA-Z0-9]_.+-]+@[A-Za-z0-9-]+\.[a-zA-Z0-9-.]+$)

import re

# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# res = pattern.search("call me at 613 600-3002")
# print(res.group())

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

def extract_all_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

# Define is_valid_time below:
def is_valid_time(input):
    time_regex = re.compile(r'\d{2}:\d{2}|\d{1}:\d{2}')
    match = time_regex.fullmatch(input)
    if match:
        return True
    return False

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())

#####################

# define parse_bytes below:
def parse_bytes(input):
    bytes_regex = re.compile(r'\b[0-1]{8}\b')
    match = bytes_regex.findall(input)
    if match:
        return match.group()

pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X | re.I)

match = pattern.search("ThomaS123@Yahoo.com")
print(match.group())
print(match.groups())

################

text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)

###################

import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
titles.sort()
fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)

    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)

#######################

print(parse_bytes("11010101 101 323"))
print(is_valid_time("1:23"))
print(is_valid_time("12:23"))
print(is_valid_time("it is 12:23"))
print(is_valid_phone("613 600-3002 ads"))
print(extract_phone("my number is 613 600-3002"))
print(extract_all_phone("my number is 613 600-3002"))
print(extract_all_phone("my number is 613 600-3002 or call me at 346 677-2888"))
