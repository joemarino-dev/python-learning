purchase_days = int(input('How many days ago have you purchased the item? '))	
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')

if is_broken == 'y':
	print('You can get a refund.')
elif purchase_days <= 10 and is_used == 'n':
	print('You can get a refund.')
else:
	print('You cannot get a refund.')	
	
# cleaner
if ((purchase_days <= 10 and is_used == 'n') or is_broken == 'y'):
	print('You can get a refund.')
else:
	print('You cannot get a refund.')
10
