# you can build lists of lists think:excel
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

print(cells[0])
print(cells[0] [0])
print(cells[0] [1])
print(cells[1] [2])

# will only reference the rows
for x in cells:
	print('Row:', x)
	
# but then you can do nested loop to get the individual cells - aka multi-dimensional lists which will be needed for things like working with tables
for x in cells:
	for y in x:
		print('Cell:', y)
		
# even clearer version
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
	for cell in row:
		print('Element:', cell)
		
# another variation
for row in table:
	for cell in row:
		print(cell, '', end='')
	print()
	
# populating a multi-dimensional list shortcut - note that you can do 3, 4, 5 dimensions but usually 1 or 2 dimensional is most common
table = [[i for i in range(1, 6)] for j in range(1, 5)]
print(table)
	

