filename = 'data/pi_digits.txt'

with open(filename) as file_object:
	# for line in file_object:
	# 	print(line.strip())
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
