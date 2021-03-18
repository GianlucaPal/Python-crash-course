def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
	return full_name.title()
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# describe_pet(animal_type='hamster', pet_name='harry')

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'quit' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'quit':
		break

	l_name = input("Last name: ")
	if l_name == 'quit':
		break
		
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")
