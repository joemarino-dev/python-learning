top_foods = ['Pizza', 'Fries', 'Gnocchi', 'Cheeseburger', 'Pork Roll', 'Sausage']

for food in top_foods:
	print('Current food:', food)
	
for food_index in range(len(top_foods)):
	print('At index', food_index, 'the food is', top_foods[food_index])
	
market_values = [10.02, 8.54, 12.90, 7.77, 6.66]
sum = 0.00
for market_value in market_values:
	sum += market_value
	
print('The market value is', sum)
