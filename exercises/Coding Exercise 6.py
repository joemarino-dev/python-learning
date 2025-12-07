python_release_year = 1994
question = 'When was Python 1.0 released? '

user_answer = int(input(question))

while user_answer != python_release_year:
	if user_answer > python_release_year:
		print('It was earlier than that!')
		user_answer = int(input(question))
	else: 
		print('It was later than that!')
		user_answer = int(input(question))
print('Correct!')
