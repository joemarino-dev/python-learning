login_data = (42, 'j75username', 'pw123')
print(len(login_data))

if '42' in login_data:
	print('Match found!')
	
for member in login_data:
	print(member)
	
login_data += ('test', 'add')
print(login_data)

numbers = (0, 1) * 10
print(numbers)

# for tuples - think here is a collection of data whose structure won't change that describe some "thing" and have mixed data types (though python doesn't enforce this) - they form a bigger object
user_data = ('Joe', 'Male', 50)

# where lists are generally a collection of similar data who typically all share same data type (though again Python doesn't restrict you)
fruits = ('Oranges', 'Bananas', 'Apples')
market_values = (45.4, 12.72, 9.8)
