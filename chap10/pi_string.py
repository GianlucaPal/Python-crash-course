filename = 'data/pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

temp = ''

pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	pos =pi_string.find(birthday)
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")

temp = pi_string[:pos-1] + '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------' + pi_string[pos:pos+6] +'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------' + pi_string[pos+6:]

print(f'....{temp}....')
print(len(pi_string))

print(pos)
