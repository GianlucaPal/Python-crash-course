bicycles = ['trek','santa cruz', 'cannondale', 'chink chonk', 'specialized']
print(bicycles[3])

poppedBicycles= bicycles.pop()
print(poppedBicycles)
print(bicycles)

bicycles.append('diamond back')
print(bicycles)

bicycles.insert(1, 'KTM')
print(bicycles)

del bicycles[4]
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)