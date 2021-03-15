pizzas = ['peperoni', 'mexicano', 'ragina']

for pizza in pizzas:
	print(f'I like {pizza.title()} pizza')

print(f'I love all pizza')

#4-2
animals= ['cat', 'dog', 'fish']

for animal in animals:
	print(f'A {animal} would make a great pet')
print(f' Any of these animals would make a great pet!')

#4-3
for value in range(1,21):
	print(value)

#4-4
numbers= list(range(1,1000001))

for number in numbers:
	print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6
oddNumbers= list(range(1,20,2))
print(oddNumbers)

#4-7
threes= list(range(3,31,3))
for three in threes:
	print(three)
#4-8
cubes= list(range(1,11))
for cube in cubes:
	cube=cube**3
	print(cube)

#4-9
cube= [value**3 for value in range(1,11)]
print(cube)

#4-10
names=['Gianluca', 'Keagan', 'Vusi', 'jerry', 'beth', 'summer']
print('\nfirst three are')

for name in names[:3]:
     print(f'{name} is good at programming')
print('\nmiddle three are')

for name in names[2:5]:
     print(f'{name} is good at programming')