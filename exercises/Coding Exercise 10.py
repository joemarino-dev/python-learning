# Requirements: Write a function that de-dups a list
# List can have any number of elements inside including empty list
# Default state of the list parameter should be empty
# Need to figure out how to identify a dup and which index to delete

def unique(source_list=[]):
	if len(source_list) == 0:
		return
	new_list = []
	for element in source_list:
		if element not in new_list:
			new_list.append(element)
	return new_list

test1 = unique([1, 1, 4, 5, 1])
print(test1)

test2 = unique(['Mark', 'Mark', 'John', 'Anne'])
print(test2)

test3 = unique()
print(test3)

# my solution works but the check for length of source list could be problematic and is unnecessary
# the loop will handle an empty list no problem and will just return empty list not None which is what I forced it to do
def unique(source_list=[]):
	new_list = []
	for element in source_list:
		if element not in new_list:
			new_list.append(element)
	return new_list

test1 = unique([1, 1, 4, 5, 1])
print(test1)

test2 = unique(['Mark', 'Mark', 'John', 'Anne'])
print(test2)

test3 = unique()
print(test3)

# and upon further research - this is not a good pattern to follow (defaulting to empty list) because that forces a shared list to be created in memory - better is to force an empty list every time (in case someone comes along and alters that default empty list)
# first example of how it could become a problem - if the code modifies source_list and then you call it multiple times - you get unexpected results
def unique(source_list=[]):
	new_list = []
	for element in source_list:
		if element not in new_list:
			new_list.append(element)
	source_list.append('TEST')
	return new_list

test1 = unique([1, 1, 4, 5, 1])
print(test1)

test2 = unique(['Mark', 'Mark', 'John', 'Anne'])
print(test2)

test3 = unique()
print(test3)

test4 = unique()
print(test4)

# better pattern - the default call always re-initializes to an empty list regardless of modifications made inside the function in the future
def unique(source_list=None):
	if source_list == None:
		source_list = []
	new_list = []
	for element in source_list:
		if element not in new_list:
			new_list.append(element)
	source_list.append('TEST')
	return new_list

test1 = unique([1, 1, 4, 5, 1])
print(test1)

test2 = unique(['Mark', 'Mark', 'John', 'Anne'])
print(test2)

test3 = unique()
print(test3)

test4 = unique()
print(test4)



