spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

months_spending_low = 0
months_spending_normal = 0
months_spending_high = 0

for spending in spendings:
	if spending < 1000.0:
		months_spending_low += 1
	elif spending <= 2500.0 and spending >= 1000.0: # while this works, you really don't need to check >= 1000 as it would have to be based on the prior check
		months_spending_normal += 1
	else:
		months_spending_high +=1
		
print('Numbers of months with low spendings: ', months_spending_low, ', normal spendings: ', months_spending_normal, ', high spendings: ', months_spending_high, '.', sep='') # this works but so will next one - no need to deal with automatic space separator when concatenating string

print('Numbers of months with low spendings: ' + str(months_spending_low) + ', normal spendings: ' + str(months_spending_normal) + ', high spendings: ' + str(months_spending_high) + '.')
