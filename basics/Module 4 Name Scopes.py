# variables can be global or local
# see below as case for same named variable having diff value inside vs outside function
# protects us when working with functions wriyten by many different devs - may use same name and don't want our vars changed unexpecredly
# aka shadowing - thr local shadows the global

def scope():
	some_variable = 'Local'
	print(some_variable)

some_variable = 'Global'
print(some_variable)
scope()
print(some_variable)

# you can change the scope though - simply by calling the function variable - global
# rarely used in practice and can do more harm than good
def scope():
	global some_variable
	some_variable = 'Local'
	print(some_variable)

some_variable = 'Global'
print(some_variable)
scope()
print(some_variable)

# a lists example - so far behaves same
def scope():
	some_variable = ['list local']
	print(some_variable)

some_variable = ['list global']
print(some_variable)
scope()
print(some_variable)

# however take note that variable scope is defined when created so if you alter and not create in function it will affect global too!
# this applies to dictionary as well but not tuple as these are immutable
def scope():
	some_variable.append('list local')
	print(some_variable)

some_variable = ['list global']
print(some_variable)
scope()
print(some_variable)
