top_foods = ['Pizza', 'Fries', 'Gnocchi', 'Cheeseburger', 'Pork Roll', 'Sausage']
print(top_foods[2])
del top_foods[2]
print(top_foods)
print(top_foods[2])

top_foods = ['Pizza', 'Fries', 'Gnocchi', 'Cheeseburger', 'Pork Roll', 'Sausage']
del top_foods[3:]
print(top_foods)

top_foods = ['Pizza', 'Fries', 'Gnocchi', 'Cheeseburger', 'Pork Roll', 'Sausage']
del top_foods[:]
print(top_foods)

top_foods = ['Pizza', 'Fries', 'Gnocchi', 'Cheeseburger', 'Pork Roll', 'Sausage']
del top_foods
# print(top_foods) # throws an error because you have deleted the entire list from existence as opposed to only deleting all the elements as we did on line 12
