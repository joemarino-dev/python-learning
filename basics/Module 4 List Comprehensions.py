# you can use loops to fill up lists, e.g., when you need a larger dataset to test agains
numbers = []
for i in range(1, 101):
	numbers.append(i)
print(numbers)

# and here's an even better shortcut way to do it
numbers = [i for i in range(1, 101)]
print(numbers)

# you can even bake in logic to make your list more sophisticated
numbers = [i for i in range(1,101) if i % 3 != 0]
print(numbers)
