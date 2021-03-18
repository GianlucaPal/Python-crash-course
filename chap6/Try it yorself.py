#6-1
classmates = {
	'gpalmarozza': {
		'first': 'gianluca',
		'last': 'palmarozza',
		'age': '18',
		'location': 'edenvale',
		},
	}

for classmateName, classmateInfo in classmates.items():
	
	full_name = f"{classmateInfo['first']} {classmateInfo['last']}"
	age = classmateInfo['age']
	location = classmateInfo['location']
	
	print(f"\tFull name: {full_name.title()}")
	print(f"\tAge: {age}")
	print(f"\tLocation: {location.title()}")

# 6-2
favoriteNumbers = {'jen': '2','sarah': '25','edward': '567','phil': '7'}

for key, value in set(favoriteNumbers.items()):
 	print(f'key: {key}, value: {value}')

# 6-3
glossary = {
'concatonate' : 'To add two strings into one', 
'camocasing' : 'to seperate words using captal letters', 
'increment' : 'an increase or addition, especially one of a series on a fixed scale.',
'string' : 'a sequence of characters, either as a literal constant or as some kind of variable',
'integer' : 'a whole number (not a fraction) that can be positive, negative, or zero.'
}

for key, value in set(glossary.items()):
 	print(f'Term: {key.title()}, Definition: {value}')

# 6-4

glossary2= {
'concatonate' : 'To add two strings into one', 
'camocasing' : 'to seperate words using captal letters', 
'increment' : 'an increase or addition, especially one of a series on a fixed scale.',
'string' : 'a sequence of characters, either as a literal constant or as some kind of variable',
'integer' : 'a whole number (not a fraction) that can be positive, negative, or zero.',
'dictionary' : 'an associative array that holds key-value pairs.',
'function' : 'a sequence of statements that may return a value to the caller',
'Key Function' : 'It is a callable that returns a value that we can use for sorting or ordering.',
' f-string' : 'An f-string is a formatted string literal.',
'Attribute' : 'An attribute is a value an object holds.',
}

for key, value in set(glossary2.items()):
 	print(f'Term: {key.title()}, Definition: {value}')

# 6-5
rivers = {'nile' : 'egypt',
		'amazon': 'south america',
		'mississippi': 'USA'}

for key, value in set(rivers.items()):
 	print(f'river: {key.title()}, country: {value}')


# 6-6
people = {'john','gianluca','jerry ','phil'}

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],}


for name in people:
	for name2 in favorite_languages.keys():
		if name == name2:
			print(f'{name} be gone')
			break
	else:
		print(f'{name} come join')

