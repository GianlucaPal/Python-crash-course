# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")


height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")