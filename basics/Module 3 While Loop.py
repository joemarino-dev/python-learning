counter = 10
while counter > 0:
	print(counter)
	counter -= 1
print('Blast off!') 

print('''
========================================
===    GUESS WHAT I/'M THINKING.     ===
========================================
''')
number = 19
guess = int(input('Guess what number I\'m thinking. HINT: Between 1 and 20: '))
while guess != 19:
	print('That is NOT correct.')
	guess = int(input('Guess what number I\'m thinking. HINT: Between 1 and 20: '))
print('You got it!')
