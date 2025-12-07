# You can put 'pass' as a simple placeholder for stubbing out code
for i in range(11):
	pass 

if i < 11:
	pass
	
# Nested loops will execute inner until satisfied then go back to outer and so on

for i in range(1, 6):
	for j in range(1, 6):
		print(i, 'x', j, '=', i * j)
		
# a loop's else branch will always get executed once regardless of # iterations of loop body\

i = 3
while i < 5:
	print(i)
	i += 1
else:
	print('else:', i)

