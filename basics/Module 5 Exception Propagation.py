def get_birth_month(user_info):
	birth_month = int(input('Enter birth month (1 - 12): '))
	user_info.append(birth_month)
	
def get_birth_day(user_info):
	birth_day = int(input('Enter day of birth: '))
	user_info.append(birth_day)
	
def get_birth_year(user_info):
	birth_year = int(input('Enter birth year (YYYY): '))
	user_info.append(birth_year)
	
def get_birth_date(user_info):
	try:
		get_birth_month(user_info)
		get_birth_day(user_info)
		get_birth_year(user_info)
		print('Your birthdate is', user_info)
	except ValueError:
		print('You entered an invalid value.')
	
print('I need your birth date.')
user_info = []
get_birth_date(user_info)
	


