favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# language2 = favorite_languages.get('sarah','no point value assigned')
# print(language2)

# for key, value in set(favorite_languages.items()):
#  	print(f'key: {key}, value: {value}')

# print(f'\naccessing keys')
# for key in favorite_languages.keys():
# 	print(f'Key: {key.title()}')

# print(f'\naccessing values')
# for values in favorite_languages.values():
# 	print(f'Values: {values.title()}')

# favoriteFoods = {'jen': 'ribs','sarah': 'pizza','edward': 'burgers','phil': 'salad'}

# print(f'\naccessing keys')
# for key in favoriteFoods.keys():
# 	print(f'Key: {key.title()}')

# print(f'\naccessing values')
# for values in favoriteFoods.values():
# 	print(f'Values: {values.title()}')

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

