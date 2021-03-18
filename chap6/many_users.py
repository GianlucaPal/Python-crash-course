# users = {
# 	'aeinstein': {
# 		'first': 'albert',
# 		'last': 'einstein',
# 		'location': 'princeton',
# 	},
# 	'mcurie': {
# 		'first': 'marie',
# 		'last': 'curie',
# 		'location': 'paris',
# 		},
# 	}

# for username, user_info in users.items():
# 	print(f"\nUsername: {username}")
# 	full_name = f"{user_info['first']} {user_info['last']}"
# 	location = user_info['location']
# 	print(f"\tFull name: {full_name.title()}")
# 	print(f"\tLocation: {location.title()}")

classmates = {
	'gpalmarozza': {
		'first': 'gianluca',
		'last': 'palmarozza',
		'location': 'edenvale',
	},
	'kdodsworth': {
		'first': 'keagan',
		'last': 'dodsworth',
		'location': 'bundus',
		},
	}

for classmateName, classmateInfo in classmates.items():
	print(f"\nUsername: {classmateName}")
	
	full_name = f"{classmateInfo['first']} {classmateInfo['last']}"
	location = classmateInfo['location']
	
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")