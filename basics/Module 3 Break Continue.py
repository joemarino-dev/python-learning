while True:
	band = input('Enter your favorite band or say "Poison" to stop: ')
	if band == 'Poison':
		break
	print('I love', band, 'too!')
	
for i in range(1, 101):
	if i % 11 == 0:
		continue
	print(i)
	
print('''
===============================
=== NUMBERS DIVISIBLE BY 19 ===
===============================
''')	
for i in range(1, 101):
	if i % 19 == 0:
		print(i)

